function blaze()
  rs.setBundledOutput("back", colours.yellow)
  term.clear()
  term.setCursorPos(1,1)
  print("Spawning Blazes")
  end
 
function skeleton()
  rs.setBundledOutput("back", colours.grey)
  term.clear()
  term.setCursorPos(1,1)
  print("Spawning Skeletons")
  end
 
function enderman()
  rs.setBundledOutput("back", colours.blue)
  term.clear()
  term.setCursorPos(1,1)
  print("Spawning Endermen")
  end
 
function witch()
  rs.setBundledOutput("back", colours.magenta)
  term.clear()
  term.setCursorPos(1,1)
  print("Spawning Witches")
  end
 
function pig()
  rs.setBundledOutput("back", colours.pink)
  term.clear()
  term.setCursorPos(1,1)
  print("Spawning Pigs")
  end
 
term.clear()
term.setCursorPos(1,1)
print("What mobs would you want to spawn?")
term.setCursorPos(1,3)
 
if read() == "blaze" //checks user input.
  then blaze()
 
elseif read() == "skeleton"
  then skeleton()
 
elseif read() == "pig"
  then pig()
 
elseif read() == "enderman"
  then enderman()
 
elseif read() == "witch"
  then witch()
 
end