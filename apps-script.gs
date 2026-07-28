/**
 * Clínica Procardíaco — captura de leads em Google Sheets (sem backend).
 *
 * COMO USAR:
 * 1. Crie uma planilha no Google Sheets.
 * 2. Menu Extensões > Apps Script. Apague o conteúdo e cole este código. Salve.
 * 3. Implantar > Nova implantação > engrenagem > "App da Web".
 *      - Executar como: Eu
 *      - Quem pode acessar: Qualquer pessoa
 * 4. Copie a URL do App da Web e cole em assets/js/site.js na variável LEAD_ENDPOINT.
 * 5. Autorize o acesso quando o Google pedir.
 *
 * Cada lead do modal de agendamento vira uma linha na aba "Leads".
 */

var SHEET_NAME = 'Leads';
var COLUMNS = [
  'timestamp', 'exame', 'data_preferida', 'periodo', 'nome', 'origem', 'pagina',
  'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
  'gclid', 'fbclid', 'referrer'
];

function doPost(e) {
  try {
    var lock = LockService.getScriptLock();
    lock.waitLock(30000);

    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sh = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
    if (sh.getLastRow() === 0) sh.appendRow(COLUMNS);

    var data = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    var row = COLUMNS.map(function (k) { return data[k] != null ? data[k] : ''; });
    sh.appendRow(row);

    lock.releaseLock();
    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService.createTextOutput('Procardiaco leads endpoint OK');
}
