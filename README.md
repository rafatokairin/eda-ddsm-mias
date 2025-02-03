# Análise Exploratória de Dados DDSM e MIAS  

Este repositório contém uma análise exploratória de dois conjuntos de dados utilizados em estudos de mamografia: **DDSM** (Digital Database for Screening Mammography) e **MIAS** (Mammographic Image Analysis Society).  

## Estrutura dos Arquivos  

### DDSM  

A análise do conjunto de dados DDSM está organizada em quatro arquivos principais:  

1. **meta.csv**  
   Contém informações gerais sobre os exames, como identificadores únicos, modalidade de imagem, descrição das séries, parte do corpo examinada, entre outros.  

2. **dicom.csv**  
   Apresenta metadados técnicos e detalhados sobre as imagens, incluindo informações sobre o formato DICOM, parâmetros técnicos das imagens e dados do paciente.  

3. **calc_case_description_test_set.csv**  
   Descreve casos relacionados a calcificações nas mamas, incluindo informações sobre o tipo de calcificação, distribuição, densidade mamária, avaliação clínica, patologia e caminhos para as imagens associadas.  

4. **mass_case_description_train_set.csv**  
   Detalha casos relacionados a massas mamárias, como forma, margens, densidade mamária, avaliação clínica, patologia e caminhos para as imagens e máscaras de região de interesse (ROI).  

### MIAS  

A análise do conjunto de dados MIAS está contida em um único arquivo:  

- **MIAS.csv**  
  Contém informações sobre as imagens do conjunto MIAS, incluindo classificações das anomalias, localização das lesões e medidas como severidade e raio das anomalias.  

# Conclusão da Análise Exploratória dos Dados do DDSM

## Resumo Geral (**calc_case_description_test_set.csv**)

A análise exploratória do conjunto de dados do *Digital Database for Screening Mammography* (DDSM) nos permitiu compreender melhor a estrutura, distribuição e relevância das variáveis disponíveis. Composto por **1546 imagens** de **602 pacientes**, o conjunto de dados apresenta características que o tornam adequado para estudos voltados à classificação de lesões mamárias como potenciais **malignas**.

## Principais Decisões e Justificativas

Durante a análise, algumas colunas foram excluídas por não contribuírem diretamente para os objetivos do projeto ou por não possuírem valor estatístico relevante. Abaixo, as principais justificativas para a exclusão:

1. **`patient_id`**: Um identificador único para cada paciente, sem impacto em análises estatísticas ou no treinamento de modelos.
2. **`abnormality_id`**: Identifica anormalidades de forma única, mas não agrega informações relevantes para padrões gerais.
3. **`image_file_path` e `cropped_image_file_path`**: Guardam os caminhos das imagens e versões recortadas, sem utilidade para análises quantitativas.
4. **`ROI_mask_file_path`**: Contém os caminhos das máscaras de regiões de interesse (ROI), úteis para processamento, mas irrelevantes na análise exploratória.
5. **`calc_type`**: Indica o tipo de calcificação. Como o foco é classificar lesões de forma geral e não por tipo, foi considerada desnecessária nesta etapa.

Essas exclusões ajudaram a focar em variáveis com maior relevância para os objetivos da análise.

## Observações das Variáveis Descritivas

Os dados foram analisados estatisticamente, com destaque para as seguintes variáveis:

- **Densidade Mamária (`Breast Density`)**:  
  A densidade do tecido mamário apresentou maior concentração nos níveis **2** e **3**. Com uma média de **2.66** e desvio padrão de **0.94**, observou-se baixa dispersão nos valores, indicando consistência nos dados.

- **Avaliação (`Assessment`)**:  
  Indicando a avaliação do exame, os valores estão concentrados entre **3** e **4**, com uma média de **3.26** e desvio padrão de **1.23**, mostrando variabilidade moderada.

- **Sutileza (`Subtlety`)**:  
  Representando o grau de dificuldade de avaliação das imagens, os valores predominantes são **3** e **4**, com uma média de **3.41** e desvio padrão de **1.18**, indicando dispersão moderada.

## Considerações Finais

1. **Objetivo do Projeto**:  
   A análise confirmou que o objetivo de classificar imagens como potencialmente **malignas** pode ser atingido com os dados disponíveis, dado que há variabilidade suficiente para treinar modelos.

2. **Importância de Dados Não Correlatos**:  
   A diversidade dos dados é essencial para garantir que o modelo aprenda características relevantes e mais profundas, evitando soluções simples baseadas em alta correlação entre variáveis.

3. **Próximos Passos**:  
   A etapa de análise exploratória forneceu uma base para os próximos passos do projeto, incluindo o processamento de imagens e o treinamento de modelos de aprendizado profundo.

## Resumo Geral (**mass_case_description_train_set.csv**)

A análise é semelhante à (**calc_case_description_test_set.csv**), porém temos **1318 imagens** de **691 pacientes**.
