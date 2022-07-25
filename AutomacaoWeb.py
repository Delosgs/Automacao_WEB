
#  Teste rápido e confiável de ponta a ponta para aplicativos web modernos

from playwright.sync_api import sync_playwright  # Usando de forma syncrona para o teste ser rodado passo a passo


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # Aqui eu inicio o chromium / Com o parametro para abrir o navegador
    page = browser.new_page() # Aqui eu mando o browser abrir uma nova página
    page.goto("http://google.com.br")
    #vou digitar linkedin no imput de texto name="q"
    page.fill("input[name='q']", 'linkedin') # aqui é o comando preencher o imput com linkedin
    #vou clicar no botão pesquisar cujo name="btnK"
    page.click("input[name='btnK']") # aqui o comando que faz clicar em pesquisar
    page.wait_for_timeout(2000) # comando para a pagina aguardar em milisegundos
    print(page.title())
    browser.close() # aqui ele fecha o navegador