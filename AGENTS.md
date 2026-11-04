# Contexto do projeto: "Checkei"

Resumo da conversa de ideação com o Claude (Cowork), 4 nov 2026. Lê isto antes de mexer no código.

- Nome da app: **Checkei** (decidido a 4 nov 2026; nome de trabalho anterior: "Já fiz?").
- Repositório: https://github.com/rubatista/checkei-app (privado).

## Regras para agentes
- **Não fazer commits, merges nem push.** O Ruben trata de tudo o que é git.

## A ideia
App para confirmar tarefas de rotina com prova. Exemplos: "fechei a porta?", "desliguei o fogão?", "tomei o comprimido?". O utilizador tira uma foto (ou marca sem foto), e o registo fica guardado com a hora exata. Quando surge a dúvida, abre a app e confirma.
- Público: pessoas com ansiedade, PHDA ou TOC, e qualquer pessoa cansada ou distraída.
- Diferencial: as apps de lembretes dizem *para fazer*. Esta dá *prova de que já fez*.
- Utilizador/dono: Ruben (Windows + WSL Ubuntu 22.04, iPhone). Idioma da app: português de Portugal.

## Visão a longo prazo (ainda NÃO implementar)
A Checkei é o primeiro módulo de uma futura app-mãe com módulos que partilham a mesma base (registos + alertas + partilha com um "círculo" familiar):
- **Cuidar**: coordenar o cuidado de pais idosos entre irmãos (medicação, consultas, notas).
- **Carga Mental**: tarefas partilhadas em casal/família que registam *quem se lembrou* de cada uma.
- **Pasta da Vida**: documentos e prazos (IUC, inspeção, seguro, Cartão de Cidadão, IRS, garantias) com leitura automática de datas.
Decisão: lançar primeiro a Checkei sozinha, mas desenhada para receber módulos mais tarde. O Ruben ainda vai decidir o caminho.

## Plano por fases
1. **MVP pessoal, sem servidor** (estado atual: protótipo feito)
2. Contas + sincronização na nuvem + "círculo" (Supabase ou Firebase)
3. Módulos Cuidar / Carga Mental / Pasta da Vida
4. Freemium (Checkei grátis; módulos familiares e nuvem pagos)
Stack sugerida para a app nativa: Expo / React Native (iOS + Android com um só código).

## Estado atual do código (protótipo PWA)
- `src/app.html`: código-fonte único (HTML + CSS + JS, sem frameworks).
- `build.py`: gera `index.html` (com meta tags de PWA para iPhone) a partir de `src/app.html`. **Editar sempre `src/app.html` e depois correr `python3 build.py`.**
- `manifest.webmanifest`, `icon-512.png`: instalação no ecrã principal.
- Correr localmente: `python3 -m http.server 8000`.

Funcionalidades implementadas:
- Cartões de estado de hoje: Porta, Fogão, Carro, Medicação, Janelas, Ferro/ficha (+ "Outro" no registo)
- Registo com foto (`<input type="file" capture="environment">`, comprimida para JPEG 1080px) ou sem foto, com nota opcional
- Linha do tempo de hoje, histórico agrupado por dia, ecrã de detalhe com carimbo de data estilo câmara antiga
- Apagar automaticamente ao fim de 1/3/7/30 dias (definição em localStorage)
- Dados em IndexedDB (`jafiz`/`rec`), com fallback em memória. As chaves internas `jafiz*` ficam com o nome antigo de propósito, para não perder registos já guardados. Nada sai do telemóvel
- Registos de exemplo (`ex: true`) na primeira abertura, com botão para os apagar
- Tema claro/escuro via tokens CSS em `:root`

## Ideias para os próximos passos
- Atalho/widget do iPhone para registar com 1 toque
- Lembrete ao sair de casa ("Confirmou a porta?") com geofencing (precisa de app nativa)
- Vídeo curto de 3 s em vez de foto
- Validar com 10 a 15 pessoas do público-alvo antes de investir em app nativa
