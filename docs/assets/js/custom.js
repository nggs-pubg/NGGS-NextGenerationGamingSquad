document.addEventListener("DOMContentLoaded", () => {
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
});
