# Checkei

Protótipo da app Checkei. Serve para registar, com foto e hora exata, que fechou a porta, desligou o fogão, tomou a medicação, etc.

## Estrutura

- `src/app.html`: código-fonte da app (HTML + CSS + JS num só ficheiro)
- `build.py`: gera o `index.html` (versão instalável no iPhone) a partir de `src/app.html`
- `index.html`, `manifest.webmanifest`, `icon-512.png`: app pronta a servir

## Correr no computador (WSL)

```bash
cd ~/Projects/checkei-app
python3 build.py          # só é preciso depois de alterar src/app.html
python3 -m http.server 8000
```

Abra http://localhost:8000 no browser do Windows.

## Testar no iPhone (mesma rede Wi-Fi)

O WSL não fica visível na rede por defeito. A forma mais simples é usar um túnel temporário:

```bash
npx localtunnel --port 8000      # ou: cloudflared tunnel --url http://localhost:8000
```

Abra o endereço que aparecer no Safari do iPhone e toque em Partilhar → «Adicionar ao ecrã principal».

## Funcionalidades (MVP)

- Cartões de estado de hoje: porta, fogão, carro, medicação, janelas, ferro/ficha
- Registo com foto (abre a câmara do iPhone) ou sem foto, com nota opcional
- Linha do tempo de hoje e histórico agrupado por dia
- Carimbo de data/hora em cada foto
- Os registos são apagados automaticamente ao fim de 1, 3, 7 ou 30 dias
- Tudo guardado localmente (IndexedDB), sem servidor

## Próximos passos possíveis

- Widget / atalho do iPhone para registar com 1 toque
- Lembrete "Saiu de casa? Confirme a porta" (geofencing)
- Passar para app nativa (Expo / React Native) quando a ideia estiver validada
