# CLAUDE.md · template de instalação do AXIOMA em Claude Code (v2.2)

> Copie este bloco para o `CLAUDE.md` do seu repositório (ou anexe ao existente) e ajuste o caminho do kit. Este arquivo transforma as regras anti-deriva de instrução em mecanismo: o agente as reencontra a cada sessão sem depender de memória de conversa.

```markdown
## Protocolo AXIOMA (obrigatório neste repositório)

Este projeto segue o protocolo AXIOMA v2.2. Kit em `./axioma/` (um idioma só carregado).

Regras de sessão:
1. Ao iniciar qualquer sessão de execução, leia nesta ordem: `axioma/pt/AXIOMA.md`,
   depois os artefatos do projeto (`skill.md` se existir, `brief.md`, `spec.md`,
   `plano.md`) e o estado atual em `dashboard-data.js`.
2. Nenhuma microetapa fecha sem: atualizar `dashboard-data.js`, atualizar
   `auditoria.md` se houve decisão ou desvio, e rodar
   `python3 axioma/tools/axioma-lint.py .` sem erros.
3. Gates humanos: pausar, apresentar o que validar e como, aguardar veredito e eco
   de julgamento (1-3 frases do humano). Nunca aprovar gate em nome do humano;
   nunca redigir o eco.
4. Commits seguem a política do nível (ver `axioma/pt/execucao.md`). Mensagem:
   `axioma(<mN>): <resultado em uma linha>`. Push só com aprovação humana.
5. Divergência entre dashboard e auditoria: auditoria vence, conta drift_event,
   corrigir o dashboard no mesmo turno.
6. Decisão nova = pausa. Lacuna vira pergunta, nunca invenção.
```

## Hook opcional (recomendado em N2/N3)

Instale o hook que bloqueia commits com lint em erro e commits de microetapa sem atualização de estado:

```bash
cp axioma/templates/hooks/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```
