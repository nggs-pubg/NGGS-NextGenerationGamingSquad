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
      • Use valores oficiais do sensor (400/800/1600) para evitar interpolação. <br />
      • A qualquer momento, clique em <em>Valores NGGS</em> para retornar ao preset recomendado de treino.
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
      A barra representa a proporção do seu eDPI em relação a um limite sugerido de 5000. Mantenha valores consistentes para replicar seus treinos em LANs.
    </p>
  </div>
</div>

## Gerar via CLI (opcional)

Se preferir manter um histórico dos cálculos em Markdown, utilize a CLI da NGGS:

```bash
nggs calc edpi --dpi 800 --sens 1.2 --saida docs/mouse/calculadora.md
```

O comando atualiza a seção **Resultado Atual** do arquivo e cria um backup `.bak` antes de sobrescrever. Ajuste `--yaw` para outros jogos se necessário.

## Como interpretar

- **eDPI (Effective DPI)**  
  - **Descrição:** produto entre DPI físico e sensibilidade do jogo.  
  - **Por que fazer:** padroniza sensibilidade ao comparar com outros títulos.  
  - **Como reverter:** retorne aos valores anteriores via CLI ou anotação manual.  
  - **Impacto esperado:** controle previsível ao alternar entre modos de mira.

- **Distância de 360°**  
  - **Descrição:** quanto o mouse precisa se deslocar para realizar uma volta completa no jogo.  
  - **Por que fazer:** ajuda a calibrar espaço do mousepad e encontrar conforto na mira.  
  - **Como reverter:** refaça o cálculo com os valores antigos ou restaure o backup `.bak`.  
  - **Impacto esperado:** movimentos mais consistentes, evitando extrapolar o mousepad em engagements rápidos.
