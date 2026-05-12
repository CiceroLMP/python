from flask import Flask

app = Flask(__name__)

@app.route('/')
def curriculo():
    return '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Cícero Lucas</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: #f0f4f8;
            color: #2d3748;
            min-height: 100vh;
            padding: 40px 16px;
        }

        .container {
            max-width: 820px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.10);
            overflow: hidden;
        }

        /* ── CABEÇALHO ── */
        .header {
            background: linear-gradient(135deg, #1a202c 0%, #2d3748 60%, #4a5568 100%);
            padding: 48px 48px 40px;
            color: #fff;
            position: relative;
        }

        .header::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 0;
            right: 0;
            height: 32px;
            background: #ffffff;
            border-radius: 32px 32px 0 0;
        }

        .header-inner {
            display: flex;
            align-items: center;
            gap: 28px;
        }

        .avatar {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
            font-weight: 700;
            color: #fff;
            flex-shrink: 0;
            border: 3px solid rgba(255,255,255,0.25);
        }

        .header-text h1 {
            font-size: 1.9rem;
            font-weight: 700;
            letter-spacing: -0.5px;
        }

        .header-text p {
            font-size: 0.95rem;
            color: rgba(255,255,255,0.65);
            margin-top: 4px;
            font-weight: 300;
        }

        /* ── CONTATOS ── */
        .contacts {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 20px;
        }

        .contact-chip {
            display: flex;
            align-items: center;
            gap: 7px;
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 999px;
            padding: 6px 14px;
            font-size: 0.82rem;
            color: rgba(255,255,255,0.9);
            backdrop-filter: blur(4px);
        }

        .contact-chip svg {
            width: 14px;
            height: 14px;
            flex-shrink: 0;
            opacity: 0.8;
        }

        /* ── CONTEÚDO ── */
        .content {
            padding: 36px 48px 48px;
        }

        /* ── SEÇÃO ── */
        .section {
            margin-bottom: 36px;
        }

        .section:last-child {
            margin-bottom: 0;
        }

        .section-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .section-icon {
            width: 38px;
            height: 38px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .section-icon svg {
            width: 20px;
            height: 20px;
        }

        .icon-blue   { background: #ebf4ff; color: #3182ce; }
        .icon-purple { background: #f3e8ff; color: #805ad5; }
        .icon-green  { background: #e6fffa; color: #2f855a; }

        .section-title {
            font-size: 1.05rem;
            font-weight: 600;
            color: #1a202c;
            letter-spacing: -0.2px;
        }

        /* ── CARDS ── */
        .card-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .card {
            background: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px 20px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
            transition: box-shadow 0.2s, transform 0.2s;
        }

        .card:hover {
            box-shadow: 0 4px 16px rgba(0,0,0,0.08);
            transform: translateY(-2px);
        }

        .card-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-top: 5px;
            flex-shrink: 0;
        }

        .dot-blue   { background: #3182ce; }
        .dot-purple { background: #805ad5; }
        .dot-green  { background: #38a169; }

        .card-body {
            flex: 1;
        }

        .card-title {
            font-size: 0.92rem;
            font-weight: 600;
            color: #2d3748;
        }

        .card-sub {
            font-size: 0.80rem;
            color: #718096;
            margin-top: 3px;
        }

        .badge {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 999px;
            font-size: 0.72rem;
            font-weight: 500;
            margin-top: 6px;
        }

        .badge-blue   { background: #ebf4ff; color: #2b6cb0; }
        .badge-purple { background: #f3e8ff; color: #6b46c1; }
        .badge-green  { background: #e6fffa; color: #276749; }

        /* ── DIVISOR ── */
        .divider {
            border: none;
            border-top: 1px solid #e2e8f0;
            margin: 32px 0;
        }

        /* ── RESPONSIVO ── */
        @media (max-width: 600px) {
            .header { padding: 32px 24px 36px; }
            .content { padding: 28px 24px 36px; }
            .header-inner { flex-direction: column; text-align: center; }
            .contacts { justify-content: center; }
            .header-text h1 { font-size: 1.5rem; }
        }
    </style>
</head>
<body>

<div class="container">

    <!-- CABEÇALHO -->
    <header class="header">
        <div class="header-inner">
            <div class="avatar">CL</div>
            <div class="header-text">
                <h1>Cícero Lucas Moreira de Paula</h1>
                <p>Estudante de Tecnologia &amp; Entusiasta de Cibersegurança</p>
                <div class="contacts">
                    <span class="contact-chip">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                        cicerolucasmp@gmail.com
                    </span>
                    <span class="contact-chip">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                        +55 (31) 9 9741-2925
                    </span>
                </div>
            </div>
        </div>
    </header>

    <!-- CONTEÚDO -->
    <main class="content">

        <!-- FORMAÇÃO ACADÊMICA -->
        <section class="section">
            <div class="section-header">
                <div class="section-icon icon-blue">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path d="M12 14l9-5-9-5-9 5 9 5z"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>
                </div>
                <span class="section-title">Formação Acadêmica</span>
            </div>
            <div class="card-list">
                <div class="card">
                    <div class="card-dot dot-blue"></div>
                    <div class="card-body">
                        <div class="card-title">Colégio Santa Marcelina</div>
                        <div class="card-sub">2º ao 6º Ano</div>
                        <span class="badge badge-blue">2016 – 2020</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-dot dot-blue"></div>
                    <div class="card-body">
                        <div class="card-title">Colégio Santa Maria Pampulha</div>
                        <div class="card-sub">7º ao 9º Ano</div>
                        <span class="badge badge-blue">2021 – 2023</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-dot dot-blue"></div>
                    <div class="card-body">
                        <div class="card-title">Colégio Cotemig</div>
                        <div class="card-sub">1º ao 3º Ano do Ensino Médio</div>
                        <span class="badge badge-blue">2024 – 2026</span>
                    </div>
                </div>
            </div>
        </section>

        <hr class="divider">

        <!-- CURSOS COMPLEMENTARES -->
        <section class="section">
            <div class="section-header">
                <div class="section-icon icon-purple">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>
                </div>
                <span class="section-title">Cursos Complementares</span>
            </div>
            <div class="card-list">
                <div class="card">
                    <div class="card-dot dot-purple"></div>
                    <div class="card-body">
                        <div class="card-title">Inglês Avançado</div>
                        <div class="card-sub">Luziana Lanna Idiomas</div>
                        <span class="badge badge-purple">Idiomas</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-dot dot-purple"></div>
                    <div class="card-body">
                        <div class="card-title">Cibersegurança</div>
                        <div class="card-sub">Cisco Networking Academy</div>
                        <span class="badge badge-purple">Segurança</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-dot dot-purple"></div>
                    <div class="card-body">
                        <div class="card-title">Hardware</div>
                        <div class="card-sub">Cisco Networking Academy</div>
                        <span class="badge badge-purple">Infraestrutura</span>
                    </div>
                </div>
            </div>
        </section>

    </main>
</div>

</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
