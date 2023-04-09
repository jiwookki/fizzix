print('''
How to check if line intersects circle?

ax + by = c -> formula for linear equation

X^2 + Y^2 = C -> formula for circle

X^2 + Y^2 <= C -> formula for solid (shaded in) circle

if at ANY point in the line x^2 + y^2 <= C then intersect

so ax+by=c and x^2 + y^2 <= C -> 2 simultaneous equations

if a, b, c, C are constants, how to evaluate (x^2 + y^2 <= C)?

hmmmmmmmmmmmmmmmmmmmmmmm
---Tangent time (not the o/a trig tangent)---

How to check intersection point(s) of 2 lines, if any?

simultaneous equations duh

then I can do the substitution
there were 3 methods right (elimination, substitution, smth) i forgot the third one :skull:
    
---Tangent time 2 ---

How to find shortest distance from line AB and point (x, y)?

If I define line CD as a line that's the shortest distance between line AB and the point, line CD will be perpendicular to the line AB

ok im back (24/03/2023)
so to find the area of a triangle with the coordinates of the points you can use the "Heron's Formula"
turns out heron 's formula is just with the side lengths

so anyway
you can find the shortest distance from line AB and point C via this method:
1. create triangle ABC and find area of triangle ABC using Heron's formula
2. shortest distance of AB from C will be perpendicular to AB. Thus we can find the distance with the reverse of the 0.5*legth*height formula: 2*(area/AB)
done

27/03 im in chinese class rn

so if I were to program this or smth

def find_shortest_distance():
    
hmmmmmmmmmmmmmmm

09/04/2023
its my holiday and im still workingo n this
i decided to just leave the circle-rectangle thing for later
im gonna focus on the other things first and then maybe ill come back if i want to or if i can

anyway Thinking Time!
how to find overlap between 2 circles hitboxes?
We have distance between the centres of 2 circles as well as the radii of both the circles.

lolol after some thinking
i have realized i am brain dead
(radius1 + radius2) - currentdistance

if result of expression is negative number, no overlap

''')
