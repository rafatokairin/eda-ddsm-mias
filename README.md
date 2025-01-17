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
