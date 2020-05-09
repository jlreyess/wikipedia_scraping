# -*- coding: utf-8 -*-
import scrapy
from  wikipedia_daily.items   import articles, article


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    def parse(self, response):

        host = self.allowed_domains[0]

        for link in response.css(".featured_article_metadata > a")[:100]:   #Se limita a 100 links para buscar

            next_page = f"https://{host}{link.attrib.get('href')}"
            
            if next_page is not None:
                # Spider ingresara a cada uno de los primeros 100 links de wikipedia feature articles
                next_page = response.urljoin(next_page)
                # Mediante cb_kwargs se pasa o envia el parametro del link para que sea guardado en el json
                request = scrapy.Request(next_page, callback = self.parse_link, cb_kwargs=dict())
                request.cb_kwargs['link_pass'] = next_page
                yield request

    def parse_link(self, response, link_pass):
                
                items = articles()
                item = article()

                items["link"] = link_pass
                item["title"] = response.xpath('//h1[@id="firstHeading"]/text()').extract(),

                item["parrafo"] = list()
                # Se selecciona el texto de p y de sus descendientes mediante Xpath, ya que wikipedia
                # trae muchos links en medio de párrafos.  Para este proyecto se necesita unicamente el texto
                # Con esta funcion xpath se puede extraer.  Algunas referencias de wikipedia vienen en otros alfabetos
                # o caracteres especiales que tambien son extraidos (codificados)
                for text in response.xpath('//div[@class="mw-parser-output"]/p/descendant-or-self::text()').extract():                        
                            item["parrafo"].append( text )
                            # Se determina el final del párrafo como un Punto y Aparte, es decir, .\n (punto y break line)
                            # Cuando se encuentra se termina el if mediante 'break' para solo seleccionar el primer parrafo
                            if '.\n' in text:
                                break

                items["body"] = item
                return items
                # El archivo json es creado en shel mediante el comando: scrapy crawl article -o links.json
                # El archivo es guardado en /wikipedia_scraping/links.json

