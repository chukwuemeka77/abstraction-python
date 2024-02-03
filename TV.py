class TV:
 def TVscreen():
  pass
 
class motherBoard(TV):
  def TVscreen(self):
   print("the motherboard holds the circuit")

class IC(TV):
      def TVscreen(self):
       print("The IC is the brain of the TV")

class Wire(TV):
      def TVscreen(self):
       print("The wire brings current to the tv screen to make it show")

class Screen(TV):
        def TVscreen(self):
         print("showing football match")
        
        
class Run(motherBoard,IC,Screen):
          pass
run=Run()
run.TVscreen()

run2=IC()
run2.TVscreen()

run3=Wire()
run3.TVscreen()

run4=Screen()
run4.TVscreen()

