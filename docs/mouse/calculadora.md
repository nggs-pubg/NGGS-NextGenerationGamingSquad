# Calculadora NGGS — eDPI e Distância de 360°

Ajuste sua sensibilidade com a ferramenta abaixo. A área interativa ocupa **800x600 px** em monitores desktop e se adapta automaticamente em telas menores.

<div class="dpi-tool" data-dpi-tool>
  <div class="dpi-tool__panel">
    <fieldset>
      <legend>Entradas</legend>
      <div class="dpi-tool__input">
        <label for="dpi">DPI do mouse</label>
        <input id="dpi" type="number" min="1" step="1" value="" placeholder="Ex.: 800" data-dpi-input />
      </div>
      <div class="dpi-tool__input">
        <label for="sens">Sensibilidade no jogo</label>
        <input id="sens" type="number" min="0" step="0.01" value="" placeholder="Ex.: 1.20" data-sens-input />
      </div>
      <div class="dpi-tool__input">
        <label for="yaw">Yaw (PUBG padrão 0.0025)</label>
        <input id="yaw" type="number" min="0" step="0.0001" value="0.0025" data-yaw-input />
      </div>
      <div class="dpi-tool__actions">
        <button type="button" data-action-default>Valores NGGS</button>
        <button type="button" data-action-reset>Limpar</button>
      </div>
    </fieldset>
    <p class="dpi-tool__details">
      • **Yaw** indica quantos graus a câmera gira por contagem de mouse. Para o PUBG utilizamos `0.0025`. <br />
      • Use valores nativos do sensor (400/800/1600) para evitar interpolação. <br />
      • Clique em <em>Valores NGGS</em> para recuperar nosso preset de conforto.
    </p>
  </div>
  <div class="dpi-tool__output">
    <h3>Resultado imediato</h3>
    <div class="dpi-tool__metrics">
      <div class="dpi-tool__metric">
        <strong>eDPI</strong>
        <span data-output-edpi>—</span>
      </div>
      <div class="dpi-tool__metric">
        <strong>Distância 360°</strong>
        <span data-output-distance>—</span>
      </div>
    </div>
    <div class="dpi-tool__chart">
      <div class="dpi-tool__chart-bar" data-output-bar></div>
      <span class="dpi-tool__chart-label">Visualização relativa</span>
    </div>
    <p class="dpi-tool__details">
      A barra mostra o tamanho do seu eDPI em relação a um limite sugerido de 5000. Manter números parecidos ajuda a sentir o mesmo controle em qualquer jogatina.
    </p>
  </div>
</div>

## Como interpretar

- **eDPI (Effective DPI)**  
  - **Descrição:** produto entre DPI físico e sensibilidade do jogo.  
  - **Por que fazer:** padroniza a sensibilidade quando você alterna entre games.  
  - **Como reverter:** anote seus valores atuais e, se não curtir, volte para eles na calculadora.  
  - **Impacto esperado:** controle previsível ao alternar entre modos de mira.

- **Distância de 360°**  
  - **Descrição:** quanto o mouse precisa se deslocar para realizar uma volta completa no jogo.  
  - **Por que fazer:** ajuda a calibrar espaço do mousepad e encontrar conforto na mira.  
  - **Como reverter:** refaça o cálculo com os valores antigos ou use sua anotação manual.  
  - **Impacto esperado:** movimentos mais consistentes, evitando extrapolar o mousepad em lutas intensas.
