# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):



  """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
"""
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())

  "*** YOUR CODE HERE ***"
  #python pacman.py -l tinyMaze -p SearchAgent
  #python pacman.py -l mediumMaze -z .7 -p SearchAgent
  #python pacman.py -l bigMaze -z .5 -p SearchAgent
  #python pacman.py -l openMaze -z .8 -p SearchAgent
  """A ordem de precedencia de direcao eh esquerda, direita, baixo e cima"""
  """Foi criado uma pilha utilizando a classe stack do 
  arquivo util para armazenar como pilha os movimentos do pacman"""
  pilha = util.Stack()
  """Responsavel por guardar os nos explorados ateh o momento"""
  nos_Explorados = []
  """Responsavel por pegar a coordenada inicial do pacman, podia botar direto na pilha
  mas fica mais didatico assim"""
  c_Inicial = problem.getStartState()
  """Responsavel por botar na pilha a coordenada inicial e uma lista de direcao
  poderia ser pilha.push((problem.getStartState(), [])
  Exemplo: ((x,y), string) sendo string a direção que o pacman ta tomando"""
  pilha.push((c_Inicial, []))
  """Enquanto a pilha nao estah completamente vazia ou nao chegar ao objetivo"""
  while not pilha.isEmpty():
      """A coordenada atual do pacman junto com as direcoes que ele tem percorrido... eh soh dar print em pacman"""
      pacman = pilha.pop()
      #print pacman
      coordenada = pacman[0]
      #print coordenada
      seq_Passos = pacman[1]
      #print seq_Passos
      """Se a coordenada for o objetivo, no caso, a comida, imprime a sequencia de passos 
      pra chegar nesse objetivo e retorna a string, no caso as direcoes tomadas pelo pacman ateh o objetivo"""
      if problem.isGoalState(coordenada):
          #print seq_Passos
          return seq_Passos
      """Se a coordenada nao estiver em nos explorados, tem que adicionar
      essa coordenada em nos explorados"""
      if coordenada not in nos_Explorados:
          nos_Explorados.append(coordenada)
          """Responsavel por verificar os sucessores possiveis do noh atual, o estado atual do pacman"""
          for aux in problem.getSuccessors(coordenada):
              #print ("Cordenada: ", coordenada)
              #print ("Sucessores: ", aux)
              """Se a coordenada do noh sucessor nao estiver em noh explorado
              eh posto na pilha a coordenada desse noh sucessor e tbm a soma de todas
              as sequencias de passos que ja foram dados ateh agora mais essa"""
              if aux[0] not in nos_Explorados:
                  pilha.push((aux[0], (seq_Passos + [aux[1]])))
  #util.raiseNotDefined()

def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"
  "*** YOUR CODE HERE ***"
  """A diferenca estah apenas na implementacao do util.Queue, que empilha as direções, tornando a precedencia
  de direção diferente, no caso, cima, baixo, direita, esquerda. O resto da funcao funciona
  da mesma maneira que a de busca em profundidade"""
  #python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  #python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
  #python pacman.py -l openMaze -z .8 -p SearchAgent -a fn=bfs
  fila = util.Queue()
  nos_Explorados = []
  c_Inicial = problem.getStartState()
  fila.push((c_Inicial, []))

  while not fila.isEmpty():
      pacman = fila.pop()
      coordenada = pacman[0]
      seq_Passos = pacman[1]

      if problem.isGoalState(coordenada):
          #print seq_Passos
          return seq_Passos
      if coordenada not in nos_Explorados:
          nos_Explorados.append(coordenada)
          for aux in problem.getSuccessors(coordenada):
              if aux[0] not in nos_Explorados:
                  fila.push((aux[0], (seq_Passos + [aux[1]])))
  #util.raiseNotDefined()
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  """A busca por custo uniforme utiliza a funcao PriorityQueue para auxiliar nossa busca,
  essa função dá pop no item de menor custo que estiver na fila"""
  #python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
  #python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
  #python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
  #python pacman.py -l openMaze -z .8 -p SearchAgent -a fn=ucs
  fila = util.PriorityQueue()
  nos_Explorados = []
  c_Inicial = problem.getStartState()
  """Tem uma diferenca aqui, ja que eh necessario acrescentar o custo, que comeca com zero, claro"""
  fila.push((c_Inicial, []), 0)

  while not fila.isEmpty():
      pacman = fila.pop()
      coordenada = pacman[0]
      seq_Passos = pacman[1]

      if problem.isGoalState(coordenada):
          #print seq_Passos
          #print custo
          #print ("Custo: ", len(seq_Passos))
          return seq_Passos
      if coordenada not in nos_Explorados:
          nos_Explorados.append(coordenada)
          for aux in problem.getSuccessors(coordenada):
              """A diferenca entre esse codigo e os outros dois acima estah no custo...
              O custo eh calculado pela funcao problem.getCostOfActions, que eh o tamanho 
              de seq_Passos... poderia ser len(seq_Passos)... 
              eh importante lembrar que no pop... o retorno eh do menor custo da fila...
              Eh assim que funciona o heapq.heappop"""
              if aux[0] not in nos_Explorados:
                  nova_Sequencia = seq_Passos + [aux[1]]
                  custo = problem.getCostOfActions(nova_Sequencia)
                  fila.push((aux[0], nova_Sequencia), custo)
  #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  """Funciona quase como o custo uniforme, mas o custo da busca A* tem que ter
  custo uniforme + custo heuristico
  O que faz com que o custo aumente mais que o custo uniforme
  O restultado disso eh que a busca, quando dado pop, verifica o caminho de
  menor custo ateh o estado atual do pacman e continua por esse caminho
  meio que ignorando os caminhos que chegue a um custo maior
  A precedencia eh o custo nesse caso... Na fila, quem eh posto na frente pela
  função PriorityQueue, são as coordenadas que possuem o menor custo ateh o momento
  do pacman
  """
  #python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  #python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  fila = util.PriorityQueue()
  nos_Explorados = []
  c_Inicial = problem.getStartState()
  fila.push((c_Inicial, []), 0)

  while not fila.isEmpty():
      pacman = fila.pop()
      coordenada = pacman[0]
      seq_Passos = pacman[1]

      if problem.isGoalState(coordenada):
          #print seq_Passos
          return seq_Passos
      if coordenada not in nos_Explorados:
          nos_Explorados.append(coordenada)
          for aux in problem.getSuccessors(coordenada):
              if aux[0] not in nos_Explorados:
                  nova_Sequencia = seq_Passos + [aux[1]]
                  custo_uniforme = problem.getCostOfActions(nova_Sequencia)
                  custo_heuristico = heuristic(aux[0], problem)
                  custo = custo_uniforme + custo_heuristico
                  fila.push((aux[0], nova_Sequencia), custo)
  #util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
