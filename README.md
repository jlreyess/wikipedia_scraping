# Wikipedia Scraping
## Codigo en Python para hacer Scraping de Wikipedia Featured Articles

Este es un código de ejemplo para utilizar una spider de Scrapy, librería de Python que se utiliza para hacer Scraping en páginas web.  Este es un ejemplo de la aplicación en el sitio de Wikipedia Feature Articles.

En este ejemplo, entramos en la página: https://en.wikipedia.org/wiki/Wikipedia:Featured_articles, y se leen 100 links de está página.  Se ingresa a cada una, y se almacena en un formato json el link, el título del artículo, y su primer párrafo.

Wikipedia trae dentro del texto varios links y caracteres especiales para la descripción de su texto.  Para lograr extraer el texto se utiliza la función response.xpath que nos ayuda a localizar los patrones dentro del html que nos retornarán los parámetros deseados.  En este caso se utiliza el parámetro 'descendant-or-self::text()' que ayuda a obtener todo el texto del párrafo.  Esto incluye caracteres especiales en otros alfabetos.

## El archivo json es creado en shel mediante el comando: scrapy crawl article -o links.json
