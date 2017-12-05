 Character-Based | Term-Based       | Corpus-Based | Knowledge-Based | XSD-Based |
-----------------|------------------|--------------|-----------------|-----------|
LCS              |Jaccard           |HAL           |lhc              |Type
Jaro             |Coseno            |LSA           |wup              |Occurrence
Jaro-Winler      |Block Distance    |ESA           |path             |
Levenshtein      |                  |              |res              |
                 |                  |              |lin              |
                 |                  |              |jcn              |


## LCS - (Longest Common SubString)

Calcula a similaridade entre duas strings baseado na maior substring continua comum em ambos

## Jaro
###### Implementado

Baseado no número e ordem dos caracteres comuns entre 2 strings.

## Jaro-Winler
###### Implementado

Extensão do Jaro que favorece strings que tem suas correspondências em seu prefixo

## Levenshtein
###### Implementado

Distância simples de edição entre duas strings

## Jaccard

Computa do número de termos compartilhados comparado com os termos totais

## Coseno

Computa o coseno entre os vetores de termos

## Block Distance

Distância de Manhatan, calcula a distância que seria percorrida para passar de um ponto de dados para o outro se um caminho em foma de grade for seguido. A distância entre dois itens é a soma das diferenças de seus componentes correspondentes.

## HAL - Hyperspace Analogue to Language

Cria um espaço semântico de co-ocorrências de palavras. Os elementos da matriz são a força da relação entre a palavra da coluna e da linha.

## LSA - Latent Semantic Analysis

Assume que as palavras tem significado similar, se elas ocorrem em partes similares do texto

## ESA - Explicit Semantic Analysis

A relação semântica é dada entre o TF-IDF dos termos e seu artigo Wikipédia correspondente

## lhc - Leacock & Chodorow
###### Implementado


## wup - Wu & Palmer
###### Implementado


## path - Path Length
###### Implementado


## res - Resnik
###### Implementado


## lin - Lin
###### Implementado


## jcn - Jiang & Conrath
###### Implementado

## XSD-Type
###### Implementado

## Occurrence
###### Implementado
