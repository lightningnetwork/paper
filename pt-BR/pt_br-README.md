# Paper da Rede Ralâmpago

Esta é a Rede Ralâmpago do Bitcoin

Arquivo PDF em: [http://lightning.network/lightning-network-paper.pdf](http://lightning.network/lightning-network-paper.pdf)
Licença: Creative Commons

#como compilar e Editar.

Paper esta no formato LaTeX. Diagramas em dia, Mas podem ser refeitos em
inkscape para limpeza.

## enviando a bibliografia.
Se você não tem familiaridade com o latex, upload da bibliografia, requisitos para execução:
```
pdflatex new.tex
bibtex new
pdflatex new.tex
pdflatex new.tex
```

## Gerando figuras
requido dia

```
cd figures
python dia2pdf.py
```

## Formatando

O formato padrao são de 80 characteres ao menos que exista um explícito
prencisando de algo maior.

Voce precisa formatacao de paragrafos, configuraçoes para vim:

```
:set tw=80
```

para redigir um texto, é assim:
```
<ESC>gqj
```

para reditar um paragrafo inteiro, é assim:
```
<ESC>gq}
```

Há alguns lugares onde o refluxo pode se quebrado (primarily in figures
where it's sensitive to linebreaks).
