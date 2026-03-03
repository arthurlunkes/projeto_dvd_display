# Simulação de Colisões - DVD Bouncing

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)

Simulação em Python com Pygame que reproduz colisões entre objetos retangulares, baseada no clássico efeito de protetor de tela do DVD.

## 📋 Descrição do Projeto

Este projeto implementa uma simulação física simples onde dois objetos retangulares se movem pela tela, colidem com as bordas e entre si. Cada colisão resulta em mudança de cor e direção dos objetos, criando um efeito visual interessante.

### Características Principais

- ✨ **Dois objetos móveis** com textos "DVD 1" e "DVD 2"
- 🎯 **Sistema de colisão** entre objetos e bordas da tela
- 🎨 **Mudança de cor aleatória** a cada colisão
- 📊 **Contador de colisões** (paredes e entre objetos)
- ♻️ **Possibilidade de reiniciar** a simulação
- 🎮 **Controles simples** via teclado

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Pygame 2.0 ou superior

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd CD_DVD
```

2. Instale as dependências:
```bash
pip install pygame
```

3. Execute o programa:
```bash
python colisao_objetos.py
```

## 🎮 Controles

| Tecla | Ação |
|-------|------|
| `ESC` | Sair do programa |
| `R` | Reiniciar a simulação |
| `X` (fechar janela) | Encerrar o programa |

## 📁 Estrutura do Projeto

```
CD_DVD/
│
├── main.py                 # Código original (simulação simples)
├── colisao_objetos.py      # Código refatorado com colisões
├── README.md               # Documentação do projeto
└── .gitignore             # Arquivos a serem ignorados pelo Git
```

## 🔧 Funcionamento Técnico

### Arquitetura do Código

O projeto foi refatorado utilizando **Programação Orientada a Objetos (POO)** com duas classes principais:

#### Classe `ObjetoMovel`
Representa um objeto retangular que se move pela tela.

**Atributos:**
- `rect`: Retângulo do pygame com posição e dimensões
- `cor`: Cor RGB do objeto
- `velocidade_x` e `velocidade_y`: Velocidades de movimento
- `texto`: Texto exibido no objeto

**Métodos principais:**
- `mover()`: Atualiza a posição do objeto
- `verificar_colisao_parede()`: Detecta e trata colisões com bordas
- `verificar_colisao_objeto()`: Detecta e trata colisões entre objetos
- `mudar_cor_aleatoria()`: Altera a cor para uma cor RGB aleatória
- `desenhar()`: Renderiza o objeto na tela

#### Classe `Jogo`
Gerencia o loop principal e a lógica do jogo.

**Atributos:**
- `objeto1` e `objeto2`: Instâncias de ObjetoMovel
- `colisoes_parede`: Contador de colisões com paredes
- `colisoes_objetos`: Contador de colisões entre objetos

**Métodos principais:**
- `processar_eventos()`: Gerencia eventos de teclado
- `atualizar()`: Atualiza a lógica do jogo
- `desenhar()`: Renderiza todos os elementos
- `executar()`: Loop principal do jogo

### Sistema de Colisões

#### Colisão com Paredes
- Quando um objeto atinge uma borda, sua velocidade é invertida
- A posição é ajustada para evitar que o objeto saia da tela
- A cor do objeto muda aleatoriamente

#### Colisão entre Objetos
- Utiliza `pygame.Rect.colliderect()` para detecção
- Implementa troca de velocidades (colisão elástica simplificada)
- Separa os objetos para evitar colisões contínuas
- Ambos os objetos mudam de cor

## 🎓 Conceitos Aplicados

- **Programação Orientada a Objetos (POO)**
  - Encapsulamento
  - Classes e métodos
  - Reutilização de código

- **Física Básica**
  - Movimento uniforme
  - Colisões elásticas
  - Conservação de momento (simplificada)

- **Desenvolvimento de Jogos**
  - Game loop
  - Tratamento de eventos
  - Renderização de gráficos
  - Detecção de colisões

## 📝 Desafio Atendido

Este projeto atende aos seguintes requisitos do desafio:

- ✅ Desenvolver dois objetos (rect) que se colidam
- ✅ Usar código refatorado de movimento de objetos (simulação DVD)
- ✅ Estruturar e documentar no README.md
- ✅ Preparado para upload no GitHub

## 🛠️ Possíveis Melhorias Futuras

- [ ] Adicionar mais objetos dinamicamente
- [ ] Implementar física de colisão mais realista
- [ ] Adicionar efeitos sonoros
- [ ] Criar diferentes modos de simulação
- [ ] Adicionar rastros de movimento
- [ ] Implementar gravidade e fricção
- [ ] Permitir interação com mouse

##  Licença

Este projeto é de livre uso para fins educacionais.

---

**Nota:** Este é um projeto educacional desenvolvido para demonstrar conceitos de programação de jogos, física básica e detecção de colisões usando Python e Pygame.
