
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  

 
</head>
<body>
  <main class="container" role="main">
    <header>
    <div
      <div>
        <h1>TransFlow AI — Intelligent Language Translation Tool🌀</h1>
        <p class="lead">Fully automated, real-time translation pipeline using <strong>Streamlit</strong>, <strong>n8n Agentic AI</strong>, and <strong>Google Gemini</strong>. Designed for fast, natural translations and a showcase of modern agentic AI workflows.</p>
        <div class="badges">
          <span class="badge">Agentic AI</span>
          <span class="badge">Streamlit</span>
          <span class="badge">n8n</span>
          <span class="badge">Google Gemini</span>
          <span class="badge">Portfolio</span>
        </div>
      </div>
    </header>
<div
    <section class="grid" aria-labelledby="overview">
      <div class="card">
        <h2 id="overview">Project Overview</h2>
        <p>TransFlow AI accepts user text through a Streamlit UI and sends it to an <strong>n8n webhook</strong>. The agentic workflow constructs prompts, calls Google Gemini LLM, and returns high-quality translations in real time.</p>
<div
        <h3>Why this is useful</h3>
        <ul>
          <li>Demonstrates agentic workflows that automate LLM logic.</li>
          <li>Integrates frontend app with cloud-hosted automation (n8n cloud).</li>
          <li>Extensible to multiple languages or LLM providers.</li>
        </ul>
<div
        <h3>Quick Features</h3>
        <ul>
          <li>Fast, AI-driven translations</li>
          <li>Minimal frontend (Streamlit) for quick prototyping</li>
          <li>n8n workflow for prompt generation & LLM orchestration</li>
          <li>Cloud-hostable webhook for production demos</li>
        </ul>
      </div>
<div
      <aside class="card" aria-labelledby="techstack">
        <h2 id="techstack">Tech Stack</h2>
        <div style="margin-bottom:10px;">
          <span class="pill">Frontend</span>
          <p>Streamlit (Python)</p>
        </div>
        <div style="margin-bottom:10px;">
          <span class="pill">Workflow / Automation</span>
          <p>n8n (Webhook → Agentic AI Node → LLM)</p>
        </div>
        <div style="margin-bottom:10px;">
          <span class="pill">LLM</span>
          <p>Google Gemini (via n8n LangChain node)</p>
        </div>
        <div style="margin-bottom:12px;">
          <span class="pill">Integrations</span>
          <p>Python requests library for HTTP; n8n cloud webhook endpoint</p>
        </div>

        

https://github.com/user-attachments/assets/e16b03b5-c6ba-4b94-8642-8b4fff1f2bbd


      
     
<div
    <section class="card" id="system-flow">
      <h2>System Flow — Step by Step</h2>
      <ol>
        <li><strong>User Input (Streamlit):</strong> Text submitted via frontend to n8n webhook.</li>
        <li><strong>n8n Webhook:</strong> Receives the request and forwards payload to Agentic AI node.</li>
        <li><strong>Agentic AI Node:</strong> Constructs translation prompt dynamically.</li>
        <li><strong>Google Gemini LLM:</strong> Returns translated output to workflow.</li>
        <li><strong>Display:</strong> Streamlit renders translation for user.</li>
      </ol>
<div
      <h3>Key Code Snippets</h3>
      <p><strong>Streamlit (app.py)</strong></p>
      <pre><code>import streamlit as st
import requests

st.title("Language Translator")
text = st.text_area("Enter text")

if st.button("Submit") and text:
    response = requests.post(
        url="https://your-n8n-webhook-url",
        json={"input": text}
    )
    if response.status_code == 200:
        st.write(response.json()["output"])
</code></pre>
    </section>
<div
    <section class="card" id="project-structure">
      <h2>Project Structure</h2>
      <pre><code>Language-Translation-Tool/
├── app.py
├── workflow.json
├── README.md
</code></pre>
    </section>
<div
    <section class="card" id="runlocal">
      <h2>How to Run Locally</h2>
      <ol>
        <li><strong>Clone repo</strong>
          <pre><code>git clone https://github.com/yourusername/TransFlow-AI-Translator.git
cd TransFlow-AI-Translator</code></pre>
        </li>
        <li><strong>Install dependencies</strong>
          <pre><code>pip install streamlit requests</code></pre>
        </li>
        <li><strong>Update webhook URL</strong>
          <p>Replace the webhook URL in <code>app.py</code> if using your own n8n instance.</p>
        </li>
        <li><strong>Run Streamlit</strong>
          <pre><code>streamlit run app.py</code></pre>
        </li>
      </ol>
      <p style="color:var(--muted)">Ensure n8n workflow is active and credentials configured.</p>
    </section>
<div
    <section class="card" id="contribute">
      <h2>Next Steps & Contributing</h2>
      <ul>
        <li>Add target language selection in UI.</li>
        <li>Support multiple LLM providers (OpenAI, Anthropic, etc.).</li>
        <li>Add caching, logging, or rate-limiting for production.</li>
        <li>Enhance UI with history, examples, and downloadable transcripts.</li>
      </ul>
    </section>
<div






    
  </main>
</body>
</html>
