const initDpiTool = () => {
  const dpiTool = document.querySelector("[data-dpi-tool]");
  if (!dpiTool) return;

  const dpiInput = dpiTool.querySelector("[data-dpi-input]");
  const sensInput = dpiTool.querySelector("[data-sens-input]");
  const yawInput = dpiTool.querySelector("[data-yaw-input]");
  const edpiOutput = dpiTool.querySelector("[data-output-edpi]");
  const distanceOutput = dpiTool.querySelector("[data-output-distance]");
  const bar = dpiTool.querySelector("[data-output-bar]");
  const resetBtn = dpiTool.querySelector("[data-action-reset]");
  const defaultsBtn = dpiTool.querySelector("[data-action-default]");

  const DEFAULTS = {
    dpi: 800,
    sens: 1.2,
    yaw: 0.0025,
  };

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

  const updateOutputs = () => {
    const dpi = parseFloat(dpiInput.value);
    const sens = parseFloat(sensInput.value);
    const yaw = parseFloat(yawInput.value);

    if (![dpi, sens, yaw].every((n) => Number.isFinite(n) && n > 0)) {
      edpiOutput.textContent = "—";
      distanceOutput.textContent = "—";
      bar.style.width = "5%";
      return;
    }

    const edpi = dpi * sens;
    const countsPerDegree = 1 / yaw;
    const inches = (countsPerDegree * 360) / edpi;
    const distanceCm = inches * 2.54;

    edpiOutput.textContent = edpi.toFixed(2);
    distanceOutput.textContent = distanceCm.toFixed(2) + " cm";

    const visualRatio = clamp(edpi / 5000, 0.08, 1);
    bar.style.width = `${visualRatio * 100}%`;
  };

  [dpiInput, sensInput, yawInput].forEach((input) => {
    input.addEventListener("input", updateOutputs);
    input.addEventListener("change", updateOutputs);
  });

  resetBtn?.addEventListener("click", () => {
    dpiInput.value = "";
    sensInput.value = "";
    yawInput.value = DEFAULTS.yaw.toString();
    updateOutputs();
  });

  defaultsBtn?.addEventListener("click", () => {
    dpiInput.value = DEFAULTS.dpi.toString();
    sensInput.value = DEFAULTS.sens.toString();
    yawInput.value = DEFAULTS.yaw.toString();
    updateOutputs();
  });

  defaultsBtn?.click();
};

const initVideoCarousels = () => {
  const carousels = document.querySelectorAll("[data-carousel]");
  if (!carousels.length) return;

  const videoFrames = new Set();
  const YT_ORIGIN = "https://www.youtube.com";

  const sendPlayerCommand = (iframe, command) => {
    if (!iframe?.contentWindow) return;

    iframe.contentWindow.postMessage(
      JSON.stringify({
        event: "command",
        func: command,
        args: [],
      }),
      YT_ORIGIN
    );
  };

  const pauseOthers = (current) => {
    videoFrames.forEach((frame) => {
      if (frame !== current) {
        sendPlayerCommand(frame, "pauseVideo");
      }
    });
  };

  const setupVideoCard = (card) => {
    const iframe = card.querySelector("[data-video-iframe]");
    if (!iframe) return;

    videoFrames.add(iframe);

    const play = () => {
      pauseOthers(iframe);
      sendPlayerCommand(iframe, "playVideo");
    };

    const pause = () => {
      sendPlayerCommand(iframe, "pauseVideo");
    };

    card.addEventListener("pointerenter", play);
    card.addEventListener("pointerleave", pause);
    card.addEventListener("focusin", play);
    card.addEventListener("focusout", pause);
    card.addEventListener(
      "touchstart",
      () => {
        play();
      },
      { passive: true }
    );
  };

  const pauseAll = () => {
    videoFrames.forEach((frame) => sendPlayerCommand(frame, "pauseVideo"));
  };

  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState !== "visible") {
      pauseAll();
    }
  });

  carousels.forEach((carousel) => {
    const viewport = carousel.querySelector("[data-carousel-viewport]");
    const slides = Array.from(carousel.querySelectorAll("[data-carousel-slide]"));
    if (!viewport || !slides.length) return;

    const prevBtn = carousel.querySelector("[data-carousel-prev]");
    const nextBtn = carousel.querySelector("[data-carousel-next]");

    let step = 0;

    const recalcStep = () => {
      if (slides.length < 2) {
        step = viewport.clientWidth;
        return;
      }

      const delta = slides[1].offsetLeft - slides[0].offsetLeft;
      step = delta > 0 ? delta : viewport.clientWidth;
    };

    const updateControls = () => {
      const maxScroll = Math.max(viewport.scrollWidth - viewport.clientWidth, 0);

      if (prevBtn) {
        prevBtn.disabled = viewport.scrollLeft <= 0;
      }

      if (nextBtn) {
        nextBtn.disabled = maxScroll === 0 || viewport.scrollLeft >= maxScroll - 1;
      }
    };

    const scrollByStep = (direction) => {
      if (!step) recalcStep();

      const maxScroll = Math.max(viewport.scrollWidth - viewport.clientWidth, 0);
      const target = Math.min(
        Math.max(viewport.scrollLeft + direction * step, 0),
        maxScroll
      );

      viewport.scrollTo({ left: target, behavior: "smooth" });
    };

    prevBtn?.addEventListener("click", () => {
      scrollByStep(-1);
    });

    nextBtn?.addEventListener("click", () => {
      scrollByStep(1);
    });

    const handleScroll = () => window.requestAnimationFrame(updateControls);
    viewport.addEventListener("scroll", handleScroll, { passive: true });

    window.addEventListener("resize", () => {
      recalcStep();
      updateControls();
    });

    recalcStep();
    updateControls();

    slides.forEach((slide) => setupVideoCard(slide));
  });
};

document.addEventListener("DOMContentLoaded", () => {
  initDpiTool();
  initVideoCarousels();
});
