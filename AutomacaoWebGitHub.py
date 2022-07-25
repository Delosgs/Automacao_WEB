

from playwright.sync_api import sync_playwright  # Usando de forma syncrona para o teste ser rodado passo a passo


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # Aqui eu inicio o chromium / Com o parametro para abrir o navegador
    page = browser.new_page() # Aqui eu mando o browser abrir uma nova página
    page.goto("https://github.com/login")
    
    page.fill("input[name='login']", 'delosgs@gmail.com') # aqui é o comando preencher o imput com linkedin
    
    page.fill("input[name='password']", 'dellavolp182') # aqui o comando que faz clicar em pesquisar
    page.wait_for_timeout(2000) # comando para a pagina aguardar em milisegundos
    page.click("input[name='commit']")
    page.wait_for_timeout(2000)
    page.screenshot(path="example.png") # Comando que printa a tela
    browser.close() # aqui ele fecha o navegador