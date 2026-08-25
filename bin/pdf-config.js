// Konfigurācija md-to-pdf rīkam, lai .md failus eksportētu
// kā GitHub stila PDF ar baltu fonu un nelielām piemalēm.
//
// Lietošana:
//   npx md-to-pdf parbaudes_darbs.md --config-file pdf-config.js

module.exports = {
  stylesheet: [
    "https://cdn.jsdelivr.net/npm/github-markdown-css@5.5.1/github-markdown-light.css",
    "https://cdn.jsdelivr.net/npm/highlight.js@11.9.0/styles/github.min.css",
  ],
  body_class: "markdown-body",
  css: `
    @page {
      margin: 10mm;
    }
    body {
      background: #ffffff;
    }
    .markdown-body {
      box-sizing: border-box;
      max-width: 900px;
      margin: 0 auto;
      padding: 0;
      background: #ffffff;
      font-size: 9.5pt;
      line-height: 1.45;
    }
    .markdown-body h1 { font-size: 1.5em; margin-top: 0; margin-bottom: 0.3em; }
    .markdown-body h2 { font-size: 1.2em; margin-top: 0.9em; margin-bottom: 0.3em; }
    .markdown-body p,
    .markdown-body ul,
    .markdown-body ol { margin-top: 0.3em; margin-bottom: 0.3em; }
    .markdown-body hr { margin: 0.7em 0; }
    .markdown-body pre { font-size: 8.5pt; padding: 8px; line-height: 1.3; margin: 0.4em 0; }
    .markdown-body code { font-size: 0.88em; }
    .markdown-body h2 {
      page-break-after: avoid;
    }
  `,
  pdf_options: {
    format: "A4",
    margin: {
      top: "10mm",
      right: "10mm",
      bottom: "10mm",
      left: "10mm",
    },
    printBackground: true,
  },
  marked_options: {
    gfm: true,
  },
};
