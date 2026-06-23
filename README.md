# ware-house6

A lightweight viewer for Extension Screenshot HTML pages. Add pages as sections — no auth, no flow builder.

## Setup

```bash
npm install
npm run dev
```

## Add a section

1. Save your Extension Screenshot HTML to `public/sections/<id>/index.html`
2. Register it in `src/sections/registry.ts`

Example:

```ts
{
  id: 'home',
  label: 'Home',
  htmlPath: '/sections/home/index.html',
}
```
