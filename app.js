// app.js - feed loader, rendering, and token builder integration
// Works with app-token.js (window.researchbandToken) for uploads and commits.

const loadBtn = document.getElementById('loadBtn');
const repoInput = document.getElementById('repoInput');
const branchInput = document.getElementById('branchInput');
const tokenInput = document.getElementById('tokenInput');
const articlesEl = document.getElementById('articles');
const articleTemplate = document.getElementById('articleTemplate');
const termInput = document.getElementById('termInput');
const termOutput = document.getElementById('termOutput');
const tokensList = document.getElementById('tokensList');
const createTokenBtnLocal = document.getElementById('createTokenBtn');

const createFromArticleBtn = document.getElementById('createFromArticleBtn');
const selectedArticleEl = document.getElementById('selectedArticle');
const metadataResult = document.getElementById('metadataResult');
const w3sKeyInput = document.getElementById('w3sKey');
const ghKeyInput = document.getElementById('ghKey');

let repoFiles = []; // {path, name, content}
let repoRef = {owner:'', repo:'', branch:'main', token:''};
let selectedArticleName = null;

// load saved keys
w3sKeyInput.value = localStorage.getItem('rb_w3s_key') || '';
ghKeyInput.value = localStorage.getItem('rb_gh_key') || '';
w3sKeyInput.addEventListener('change', (e)=> localStorage.setItem('rb_w3s_key', e.target.value.trim()));
ghKeyInput.addEventListener('change', (e)=> localStorage.setItem('rb_gh_key', e.target.value.trim()));

loadBtn && loadBtn.addEventListener('click', async () => {
  const repo = (repoInput.value || '').trim();
  if (!repo || !repo.includes('/')) {
    alert('Enter repository in owner/repo format');
    return;
  }
  const [owner, repoName] = repo.split('/');
  repoRef.owner = owner;
  repoRef.repo = repoName;
  repoRef.branch = branchInput.value.trim() || 'main';
  repoRef.token = tokenInput.value.trim();
  await loadOFolder();
  renderArticles();
});

async function ghFetch(path){
  const headers = { 'Accept': 'application/vnd.github.v3+json' };
  if (repoRef.token) headers['Authorization'] = 'token ' + repoRef.token;
  const url = `https://api.github.com/repos/${repoRef.owner}/${repoRef.repo}/contents/${path}?ref=${repoRef.branch}`;
  const res = await fetch(url, { headers });
  if (!res.ok) {
    throw new Error('GitHub API error: ' + res.status + ' ' + (await res.text()));
  }
  return await res.json();
}

async function loadOFolder(){
  articlesEl.innerHTML = '<div class="card">Loading /o directory...</div>';
  try {
    const listing = await ghFetch('o');
    if (!Array.isArray(listing)) throw new Error('/o is not a dir or empty');
    const fileEntries = listing.filter(f => f.type === 'file' && /\.(txt|md|markdown)$/i.test(f.name));
    repoFiles = [];
    for (const f of fileEntries) {
      const fileJson = await ghFetch('o/' + f.name);
      const content = atob(fileJson.content.replace(/\n/g,''));
      repoFiles.push({ path: 'o/' + f.name, name: f.name, content });
    }
    logTerm(`Loaded ${repoFiles.length} articles from /o`);
  } catch (err) {
    articlesEl.innerHTML = `<div class="card">Error loading /o: ${escapeHtml(err.message || err)}</div>`;
    console.error(err);
  }
}

function renderArticles(filter='all'){
  articlesEl.innerHTML = '';
  const files = repoFiles.filter(f => {
    if (filter === 'all') return true;
    return inferColorTags(f.content).includes(filter);
  });
  for (let i=0;i<files.length;i++) {
    const f = files[i];
    const node = articleTemplate.content.cloneNode(true);
    node.querySelector('.title').textContent = f.name;
    node.querySelector('.meta').textContent = f.path;
    const parsed = renderContentWithLinks(f.content);
    node.querySelector('.content').innerHTML = parsed.html;
    const tagsNode = node.querySelector('.tags');
    const tags = parsed.tags;
    for (const t of tags) {
      const span = document.createElement('span');
      span.className = 'tag ' + t;
      span.textContent = t;
      tagsNode.appendChild(span);
    }
    const articleEl = node.querySelector('article');
    articlesEl.appendChild(articleEl);
  }
  attachArticleActions();
}

function inferColorTags(content){
  const tags = new Set();
  const lower = content.toLowerCase();
  if (/\[tag:green\]/.test(lower) || /\btool(s|ing)?\b|\bengineer(ing)?\b/.test(lower)) tags.add('green');
  if (/\[tag:orange\]/.test(lower) || /\bceo\b|\bexecutive\b|\bstrategy\b/.test(lower)) tags.add('orange');
  if (/\[tag:blue\]/.test(lower) || /\binput\b|\bsubmit\b|\bform\b/.test(lower)) tags.add('blue');
  if (/\[tag:yellow\]/.test(lower) || /\bextract\b|\bexport\b|\bdownload\b/.test(lower)) tags.add('yellow');
  if (/\[tag:red\]/.test(lower) || /\broute\b|\broutes\b|\bpath(s)?\b/.test(lower)) tags.add('red');
  if (/\[tag:pink\]/.test(lower) || /\binvestigate\b|\binvestigat(e|ion)\b|\bprobe\b/.test(lower)) tags.add('pink');
  if (/\[tag:purple\]/.test(lower) || /\bassimilate\b|\bassimilation\b|\bassimilat(e|ion)\b/.test(lower)) tags.add('purple');
  if (tags.size === 0) tags.add('green');
  return Array.from(tags);
}

function renderContentWithLinks(content){
  const names = repoFiles.map(f => f.name);
  let html = escapeHtml(content);
  // link file name occurrences
  names.forEach(name => {
    const safe = name.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
    const re = new RegExp(safe, 'g');
    html = html.replace(re, `<a href="#" data-fname="${name}" class="article-link">${name}</a>`);
  });

  const colorMap = {
    green: '\\b(tool|engineering|engineer|api|cli)\\b',
    orange: '\\b(ceo|executive|c-suite|strategy)\\b',
    blue: '\\b(input|submit|form|enter)\\b',
    yellow: '\\b(extract|export|download|scrape)\\b',
    red: '\\b(route|routes|path|branch)\\b',
    pink: '\\b(investigate|investigation|probe|detect)\\b',
    purple: '\\b(assimilate|assimilation|sync|merge)\\b'
  };
  for (const [cls, pattern] of Object.entries(colorMap)) {
    const re = new RegExp(pattern, 'ig');
    html = html.replace(re, (m) => `<span class="${cls}">${m}</span>`);
  }

  const tags = inferColorTags(content);

  // delay adding handlers to ensure DOM exists
  setTimeout(() => {
    document.querySelectorAll('.article-link').forEach(a => {
      a.onclick = (ev) => {
        ev.preventDefault();
        const fname = a.getAttribute('data-fname');
        openArticleByName(fname);
      };
    });
    document.querySelectorAll('.green, .orange, .blue, .yellow, .red, .pink, .purple').forEach(el => {
      el.onclick = (ev) => {
        const cls = Array.from(el.classList).find(c => ['green','orange','blue','yellow','red','pink','purple'].includes(c));
        if (cls) filterByTag(cls);
      };
    });
  }, 50);

  return { html, tags };
}

function openArticleByName(name){
  const f = repoFiles.find(r => r.name === name);
  if (!f) {
    logTerm(`Article ${name} not found`);
    return;
  }
  const w = window.open('', '_blank', 'width=900,height=700');
  const doc = w.document;
  doc.title = name;
  const style = doc.createElement('style');
  style.textContent = 'body{font-family:Inter,Arial;background:#071320;color:#eaf6ff;padding:20px}pre{white-space:pre-wrap} .green{background:#2ecc71;color:#021007;padding:2px 6px;border-radius:4px} .orange{background:#e67e22;color:#2b1200;padding:2px 6px;border-radius:4px} .blue{background:#3498db;color:#021a2b;padding:2px 6px;border-radius:4px} .yellow{background:#f1c40f;color:#2b2000;padding:2px 6px;border-radius:4px} .red{background:#e74c3c;color:#2b0500;padding:2px 6px;border-radius:4px} .pink{background:#ff66b3;color:#2b021a;padding:2px 6px;border-radius:4px} .purple{background:#9b59b6;color:#1b0b1b;padding:2px 6px;border-radius:4px} a{color:#8fbffd}';
  doc.head.appendChild(style);
  const h = doc.createElement('h1'); h.textContent = name;
  doc.body.appendChild(h);
  const meta = doc.createElement('div'); meta.textContent = f.path; meta.style.opacity = 0.8; doc.body.appendChild(meta);
  const parsed = renderContentWithLinks(f.content);
  const pre = doc.createElement('pre');
  pre.innerHTML = parsed.html;
  doc.body.appendChild(pre);
  // add actions to window for create token
  const actions = doc.createElement('div'); actions.style.marginTop = '12px';
  const createBtn = doc.createElement('button');
  createBtn.textContent = 'Create token from this article (opens in main window)';
  createBtn.onclick = () => {
    // communicate back to opener
    if (window.opener && window.opener.receiveArticleCreate) {
      window.opener.receiveArticleCreate(f.name);
      alert('Requested token creation in main window. Return to main window to continue.');
    } else {
      alert('Main window cannot be reached. Copy article name and use Create token in main UI.');
    }
  };
  actions.appendChild(createBtn);
  doc.body.appendChild(actions);
}

function attachArticleActions(){
  const pickBtns = document.querySelectorAll('.pickArticleBtn');
  const createBtns = document.querySelectorAll('.createTokenBtn');
  pickBtns.forEach((btn, idx) => {
    btn.onclick = () => {
      const art = repoFiles[idx];
      selectedArticleName = art.name;
      selectedArticleEl.textContent = `Selected: ${art.name}`;
      logTerm(`Selected ${art.name}`);
    };
  });
  createBtns.forEach((btn, idx) => {
    btn.onclick = () => {
      const art = repoFiles[idx];
      selectedArticleName = art.name;
      selectedArticleEl.textContent = `Selected: ${art.name}`;
      createTokenFromArticle(art);
    };
  });
}

// allow popup to request creation
window.receiveArticleCreate = (name) => {
  const f = repoFiles.find(x => x.name === name);
  if (f) createTokenFromArticle(f);
  else logTerm(`Requested article ${name} not found in main window`);
};

function escapeHtml(unsafe) {
  return (unsafe || '').replace(/[&<"']/g, function(m) {
    switch(m) {
      case '&': return '&amp;';
      case '<': return '&lt;';
      case '"': return '&quot;';
      case "'": return '&#039;';
      default: return m;
    }
  });
}

function logTerm(msg){
  const now = new Date().toISOString();
  termOutput && (termOutput.innerText += `[${now}] ${msg}\n`);
  if (termOutput) termOutput.scrollTop = termOutput.scrollHeight;
}

// Terminal commands
termInput && termInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    const v = termInput.value.trim();
    termInput.value = '';
    handleCommand(v);
  }
});

function handleCommand(cmd){
  logTerm(`> ${cmd}`);
  const parts = cmd.split(/\s+/);
  const c = parts[0].toLowerCase();
  if (c === 'help') {
    logTerm('Commands: help, list, read <filename>, create-token-from <filename>');
  } else if (c === 'list') {
    repoFiles.forEach(f => logTerm(f.name));
  } else if (c === 'read') {
    const name = parts.slice(1).join(' ');
    openArticleByName(name);
  } else if (c === 'create-token-from') {
    const name = parts.slice(1).join(' ');
    const art = repoFiles.find(f => f.name === name);
    if (art) createTokenFromArticle(art);
    else logTerm('Article not found: ' + name);
  } else {
    logTerm('Unknown command; type help for commands');
  }
}

// local token wallet
function getLocalTokens(){
  const raw = localStorage.getItem('rb_tokens');
  return raw ? JSON.parse(raw) : [];
}
function saveLocalTokens(arr){ localStorage.setItem('rb_tokens', JSON.stringify(arr)); }
function createTokenLocal(name){
  const tokens = getLocalTokens();
  const token = { name, id: 'tk_' + Math.random().toString(36).slice(2,9), created: Date.now() };
  tokens.push(token);
  saveLocalTokens(tokens);
  renderTokens();
  logTerm(`Created token ${token.name} (${token.id})`);
}
createTokenBtnLocal && createTokenBtnLocal.addEventListener('click', () => {
  const name = prompt('Token name?') || `token-${Date.now()}`;
  createTokenLocal(name);
});
function renderTokens(){
  tokensList.innerHTML = '';
  const tokens = getLocalTokens();
  tokens.forEach(t => {
    const li = document.createElement('li');
    li.textContent = t.name + (t.metadataCid ? ` (cid:${t.metadataCid})` : '') + (t.commitUrl ? ` (commit:${t.commitUrl})` : '');
    tokensList.appendChild(li);
  });
}
renderTokens();

// create metadata from article and upload/commit as requested
async function createTokenFromArticle(article) {
  logTerm(`Creating token from ${article.name}`);
  const title = `ResearchToken - ${article.name}`;
  const excerpt = article.content.slice(0, 400);
  const metadata = {
    name: title,
    description: `Token created from research article ${article.name}\n\nExcerpt:\n${excerpt}`,
    article_file: article.path,
    created_by: (window.researchbandToken && window.researchbandToken.providerInfo().userAddress) || 'anonymous',
    created_at: new Date().toISOString(),
    research_snippet: article.content.slice(0, 2000)
  };
  metadataResult.innerHTML = `<pre>${JSON.stringify(metadata, null, 2)}</pre>`;

  // choose upload method(s)
  const w3sKey = w3sKeyInput.value.trim() || localStorage.getItem('rb_w3s_key') || '';
  const ghKey = ghKeyInput.value.trim() || localStorage.getItem('rb_gh_key') || '';

  // persist keys optionally
  if (w3sKey) localStorage.setItem('rb_w3s_key', w3sKey);
  if (ghKey) localStorage.setItem('rb_gh_key', ghKey);

  // 1) IPFS via Web3.Storage
  if (w3sKey) {
    metadataResult.innerHTML += `<div>Uploading metadata to IPFS via Web3.Storage...</div>`;
    try {
      const cid = await window.researchbandToken.uploadMetadataToW3s(w3sKey, metadata);
      const url = `https://ipfs.io/ipfs/${cid}`;
      metadataResult.innerHTML += `<div>IPFS CID: <a href="${url}" target="_blank">${cid}</a></div>`;
      // save token record locally
      const tokens = getLocalTokens();
      tokens.push({ name: metadata.name, sourceArticle: article.name, metadataCid: cid, created_at: Date.now() });
      saveLocalTokens(tokens);
      renderTokens();
      logTerm(`Uploaded metadata to IPFS: ${cid}`);
    } catch (err) {
      metadataResult.innerHTML += `<div style="color:orange">IPFS upload failed: ${err.message || err}</div>`;
      console.error(err);
    }
  }

  // 2) Commit metadata to GitHub repo if token provided
  if (ghKey) {
    metadataResult.innerHTML += `<div>Committing metadata JSON to repo (tokens/metadata/)...</div>`;
    try {
      const slug = article.name.replace(/\s+/g,'-').replace(/[^a-zA-Z0-9-_.]/g,'').toLowerCase();
      const filename = `tokens/metadata/${Date.now()}-${slug}.json`;
      const contentStr = JSON.stringify(metadata, null, 2);
      const res = await window.researchbandToken.commitMetadataToRepo(ghKey, repoRef.owner, repoRef.repo, repoRef.branch, filename, contentStr);
      // res.content.html_url may exist
      const commitUrl = res.content && res.content.html_url ? res.content.html_url : '';
      metadataResult.innerHTML += `<div>Committed to: <a href="${commitUrl}" target="_blank">${commitUrl || filename}</a></div>`;
      const tokens = getLocalTokens();
      tokens.push({ name: metadata.name, sourceArticle: article.name, commitUrl, path: filename, created_at: Date.now() });
      saveLocalTokens(tokens);
      renderTokens();
      logTerm(`Committed metadata to repo: ${filename}`);
    } catch (err) {
      metadataResult.innerHTML += `<div style="color:orange">GitHub commit failed: ${err.message || err}</div>`;
      console.error(err);
    }
  }

  if (!w3sKey && !ghKey) {
    metadataResult.innerHTML += `<div style="color:orange">No storage key provided. Saved token locally as draft.</div>`;
    const tokens = getLocalTokens();
    tokens.push({ name: metadata.name, sourceArticle: article.name, metadata });
    saveLocalTokens(tokens);
    renderTokens();
  }
}

createFromArticleBtn && createFromArticleBtn.addEventListener('click', () => {
  if (!selectedArticleName) {
    alert('Select an article first');
    return;
  }
  const art = repoFiles.find(a => a.name === selectedArticleName);
  if (art) createTokenFromArticle(art);
});

// filters
const filters = document.getElementById('filters');
filters && filters.addEventListener('click', (e) => {
  const btn = e.target.closest('button');
  if (!btn) return;
  const f = btn.getAttribute('data-filter');
  filterByTag(f);
});
function filterByTag(tag){
  if (tag === 'all') renderArticles('all');
  else renderArticles(tag);
  logTerm(`Filtered by: ${tag}`);
}