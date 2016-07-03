import random
import numpy
import time
import sys
def randi(num, num0):
   return random.randrange(num, num0) 

def randf(num, num0):
   return random.randrange(num, num0) * random.random()

def repl(words, word, spot):
   wdlist = words.split()
   wdlist.pop(spot)
   wdlist.insert(spot, word)
   return " ".join(wdlist) 
   
pirate_count = randi(3, 13)
location = range(randi(30, 200))

types = ['organic', 'cybernetic']
parts = ['Head', 'Leg', 'Arm', 'Torso']
bad_organic = [ 'Rotting', 'Weak', 'Decomposed', 'Damaged', 'Ravaged', 'Torn', 'Burnt', 'Lacerated', 'Gory', 'Punctured']
good_organic = [ 'Sterilized', 'Fresh', 'Strong', 'Excellent', 'Enhanced', 'Bioformed', 'Mutated', 'Preserved']
bad_cyber = ['Shoddy', 'Damaged', 'Exposed', 'Novice', 'Fried', 'Ionic', 'Basic', 'Cheap', 'Simple', 'Obsolete'] 
good_cyber = ['Embedded', 'Multi-core', 'Parallel', 'Advanced', 'Covalent', 'Resonating', 'Computerized', 'Military-Grade']
gender = ['Male', 'Female'] 
corpses = ['Scientist', 'Engineer', 'Soldier', 'Guard', 'Pirate', 'Criminal', 'Drunk', 'Officer', 'Dancer', 'Pilot', 'Botanist', 'Chef']
class Part():
   integrity = 0.0
   armor = 0.0
   damage = 0.0
   type = ''
   name = ''
   slot = ''

   def __init__(self, partname=''):
      self.type = types[random.randrange(0,2)]
      qual = random.randrange(0,10)
      if self.type == 'organic':
         if qual <= 7:
            self.name = " ".join((bad_organic[randi(0,len(bad_organic))], parts[randi(0,len(parts))])) 
            self.integrity = randf(1,7)
            self.armor = randf(0,5)
            self.damage = randf(0,3)
         else:
             self.name = " ".join((good_organic[randi(0, len(good_organic))], parts[randi(0,len(parts))]))
             self.integrity = randf(3,10)
             self.armor = randf(1,5)
             self.damage = randf(0,5)
      else:
         if qual <= 7:
            self.name = " ".join((bad_cyber[randi(0,len(bad_cyber))], parts[randi(0,len(parts))]))  
            self.integrity = randf(2,7) 
            self.armor = randf(0,8)
            self.damage = randf(1,5)
         else:
             self.name = " ".join((good_cyber[randi(0,len(good_cyber))], parts[randi(0,len(parts))]))  
             self.integrity = randf(5,11) 
             self.armor = randf(4,14)
             self.damage = randf(3,20)
      if len(partname) > 0:
         self.name = repl(self.name, partname, 1)



class Body:
   head = ''
   torso = ''
   l_arm = ''
   r_arm = ''
   l_leg = ''
   r_leg = ''
   name = ''
   
   def __init__(self):
      self.head = Part('Head')
      self.name = " ".join([gender[randi(0,2)], corpses[randi(0, len(corpses))]]) 
      self.torso = Part('Torso')
      self.l_arm = Part('Arm') 
      self.r_arm = Part('Arm')
      self.l_leg = Part('Leg')
      self.r_leg = Part('Leg') 
      


class Creation:
  body = ''
  health = 0.0
  armor = 0.0
  attack = 0.0

  def __init__(self, body):
      setattr(self, 'body', body)
      for i, k in self.body.__dict__.iteritems():
         try:
            self.health += k.integrity
            self.armor += k.armor
            self.attack += k.damage
         except:
            continue
   
random.seed()




def init_bin(bin, amount):
   for i in range(amount):
      bin.append(Part())
   return bin 

def corpse_bin(bin, amount):
   for i in range(amount):
      bin.append(Body())
   return bin


def show_corpses(corpses):
   cc = 0
   for i in corpses:
      print '{0}: {1}\n'.format(cc, i.name)
      cc += 1

def show_creations(creations):
   cc = 0
   for i in creations:
      print '{0}: {1}\n'.format(cc, i.body.name)
      cc += 1


def show_parts(parts):
   cc = 0
   for i in parts:
      print '{0}: {1}\n'.format(cc, i.name)   
      cc += 1

def show_body(body):
   print body.name
   for i, k in body.__dict__.iteritems():
      try:
         print '{0}'.format(i)
         print '================================='
         for j, l in k.__dict__.iteritems():
            print '{0}:{1}'.format(j, l)
            print '------------'
         print '================================='
      except Exception as e:
         print e
         continue


def parts_specs(part):
   for i, k in part.__dict__.iteritems():
      print "{0}:{1}".format(i, k)

def create_monster(body, parts_bin):
   print 'Selected corpse:{0}'.format(body.name)
   this = raw_input('Show corpse specs?')
   if this == 'y':
      show_body(body)

   this = raw_input('Show parts available?')
   if this == 'y':
      show_parts(parts_bin)
   while this is not 'finish':
      this = raw_input('Select Option\n0: Replace Parts\n1: Remove Parts\n2: Name Creation\nfinish: Finish')
      if this == '0':
         show_body(body)
         sel = raw_input('Select Part:0: Head\n1: Torso\n2: Left Arm\n3: Right Arm\n4: Left Leg\n5: Right Leg')
         body_dict = {'0': 'head', '1' : 'torso', '2' : 'l_arm', '3' : 'r_arm', '4': 'l_leg', '5' : 'r_leg'}
         op = ''
         while op != 'y':
            show_parts(parts_bin)
            sel2 = raw_input('Select the part number you want to look at\n')
            parts_specs(parts_bin[int(sel2)]) 
            op = raw_input('Use this part?') 
         print 'Engaging in horrific surgery -- spare parts will be in parts bin'
         time.sleep(4)
         for item, item2 in body_dict.iteritems():
            if item == sel:
               print 'got it'
               wait = getattr(body, item2)
               setattr(body, item2, parts_bin[int(sel2)])
               print parts_bin[int(sel2)]
               parts_bin[int(sel2)] = wait
         show_body(body)
       
      elif this == '2':
         name = raw_input('Enter new name')
         setattr(body,'name',name)
         show_body(body)

      elif this == 'finish':
         return body     

def combat(creation1,creation2, corpse_bin, creations):
   h1 = creation1.health
   h2 = creation2.health
   global pirate_count
   while h1 > 0 and h2 > 0:
      attack1 = creation1.attack - creation2.armor
      attack2 = creation2.attack - creation1.armor
      print 'attack1 {0} attack2 {1}'.format(attack1, attack2)
      if attack1 < 0 and attack2 < 0:
         turn = randi(0,2)
         if turn == 0:
            h2 = 0.0
            break
         else:
            h1 == 0.0
            break
      turn = randi(0,2)
      if turn == 1:
         h2 -= attack1
      elif turn == 0:
        h1 -= attack2
      print h1, h2 
   if h2 < 0.0:
      print '{0} died! Adding to corpse bin'.format(creation2.body.name)
      corpse_bin.append(creation2.body)
      pirate_count -= 1
      return
   else:
     print '{0} died fighting {1}'.format(creation1.body.name, creation2.body.name)
     creations.pop(creations.index(creation1))
     return

def take_turn(creation, parts_bin, corpse_bin, pirates, creations):
   room = player_room
   global location
   while room == player_room:
      room = location[randi(0,len(location))]
   print '{0} wanders into room {1}....'.format(creation.body.name, room)
   action = randi(0,15)
   if action < 4:
      corpse = Body()
      print 'A {0} corpse has been recovered!'.format(corpse.name)
      corpse_bin.append(corpse)
      return
   elif action < 10:
      parts = Part()
      print '{0} returns with a {1}!'.format(creation.body.name, parts.name)
      parts_bin.append(parts)
      return
   else:
      print '{0} attacks a pirate!'.format(creation.body.name) 
      combat(creation,pirates[randi(0,len(pirates))], corpse_bin, creations)
      return

ah = []
corpse_bin(ah, 3)
al = []
init_bin(al, 5)
show_corpses(ah)
pirates = []
creations = []
for i in range(pirate_count):
   pirates.append(Creation(Body()))
   pirate_name = getattr(pirates[i].body, 'name')
   pirate_name = repl(pirate_name, 'Pirate', 1)
   setattr(pirates[i].body, 'name', pirate_name) 




 
print 'Current ship size: {0} squares'.format(len(location))
player_room = location[randi(0,len(location))]
print 'You are in room {0}'.format(player_room)
print 'Amount of pirates: {0}'.format(pirate_count)
alive = 1
while alive == 1 and pirate_count > 0:
   turns = 3
   while turns != 0:
      print '0: Create Monstrosity\n1: Send Out Monstrosities\n'
      command = raw_input('Your orders, Doctor?>')
      if command == '0':
         show_corpses(ah)
         op = raw_input('Select Corpse>')
         creations.append(Creation(create_monster(ah[int(op)], al)))
         ah.pop(int(op))
         print 'Monstrosity Created!'
      elif command == '1':
          if len(creations) > 0:
             show_creations(creations)
             chosen = raw_input('Choose a creation>')
             take_turn(creations[int(chosen)], al, ah, pirates, creations)    
      turns -= 1
   print 'Pirate turn'
   for i in range(pirate_count):
      num = randi(0,len(location))
      if num == player_room:
         print 'Pirates found you! You are dead!!'
         sys.exit()
     




print 'You killed all the pirates!'




