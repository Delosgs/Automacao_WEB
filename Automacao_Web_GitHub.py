from playwright.sync_api import sync_playwright  


with sync_playwright() as p: # O with faz o gerenciamento do código abrindo e fechando. Com isso vc evita de esquecer de fechalo.
    browser = p.chromium.launch(headless=False) # Aqui eu inicio o chromium / Com o parametro para abrir o navegador
    page = browser.new_page() # Aqui eu mando o browser abrir uma nova página
    page.goto("https://github.com/login")
    
    page.fill("input[name='login']", 'delosgs@gmail.com') # aqui é o comando para preencher o login
    
    page.fill("input[name='password']", 'dellavolp182') # aqui é o comando para preencher o password
    page.wait_for_timeout(1000) # comando para a pagina aguardar em milisegundos
    page.click("input[name='commit']")
    page.click('body > div.application-main > div > aside > div > div.mb-3.Details.js-repos-container.mt-5 > div > ul > li:nth-child(1) > div > div > a')
    page.wait_for_timeout(1000)
    page.click('#repository-container-header > div.d-flex.mb-3.px-3.px-md-4.px-lg-5 > div > div > span.author.flex-self-stretch > a')
    page.wait_for_timeout(1000)
    page.screenshot(path="example.png") # Comando que printa a tela
    browser.close() # aqui ele fecha o navegador