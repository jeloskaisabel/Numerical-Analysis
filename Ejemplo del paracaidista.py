
from manim import *
from math import tanh

global  speedcolor
global  carcolor
global  dragcolor

speedcolor=BLUE
carcolor=GREEN
dragcolor=RED
fvcolor = BLUE
fdcolor = GREEN

class MathModelDefinition(Scene):
    def construct(self):
        textEq=Tex(
            "Variable dependiente ","="," f(","variables independientes\\\\","parámetros",", ","funciones de fuerza",")"
        )
        self.play(Write(textEq), run_time = 5)
        for i in range(len(textEq)):
            if i == 0 or i==3 or i==4 or i==6:
                self.play(Indicate(textEq[i]))
                if i == 0:
                    self.wait(2.5)
                else:
                    self.wait(.5)    
        self.play(FadeOut(textEq))

class MathModelConcepts0(Scene):
    def construct(self):
        titles = Tex(
            "Variable dependiente ","Variables independientes","Parámetros","Funciones de fuerza", color=YELLOW
        )
        concepts = Tex("comportamiento o estado", "tiempo y espacio","reflejo de propiedades", "influencias", font_size=40
        )
        
        for i in range(len(titles)):
            titles[i].shift(2*LEFT)
            concepts[i].next_to(titles[i], DOWN)
            self.play(
                Write(titles[i]),
                FadeIn(concepts[i], shift=DOWN),
            )
            group = Group(titles[i], concepts[i])
            if i == 0:
                self.play(group.animate.scale(0.75).move_to(3*RIGHT + UP * 2.5))
            else:
                self.play(group.animate.scale(0.75).next_to(concepts[i-1], DOWN))

class MathModelConcepts(Scene):
    def construct(self):
        titles = Tex(
            "Variable dependiente ","Variables independientes","Parámetros","Funciones de fuerza", color=YELLOW, font_size=70
        )
        concepts = Tex(
            "comportamiento o estado","tiempo y espacio","reflejo de propiedades","exterior"
        )
        for i in range(len(titles)):
            VGroup(titles[i], concepts[i]).arrange(DOWN)
            self.play(
                Write(titles[i]),
                FadeIn(concepts[i], shift=DOWN),

            )
            if i == 0:
                self.wait(7)
            elif i == 1:
                self.wait(7.5)
            elif i == 2:
                self.wait(4)
            else:
                self.wait(1)            
            self.play(FadeOut(titles[i]),FadeOut(concepts[i]))
class SimpleToComplicated(Scene):
    def construct(self):
        cap1 = Tex("Simple relación algebraica", font_size=40, color=BLUE)
        cap2 = Text("Conjunto de ecuaciones diferenciales", font_size=35, color=BLUE)
        
        simpleEq = MathTex("E &= mc^{2}", font_size = 80)
        compEq = ImageMobject("compequation.png")
        compEq.set_height(5)
        cap1.next_to(simpleEq, DOWN)
        cap2.next_to(compEq, DOWN)
        self.play(Write(simpleEq), FadeIn(cap1))
        self.wait(3)
        self.play(FadeOut(simpleEq), FadeOut(cap1))
        self.play(FadeIn(compEq),FadeIn(cap2))
        self.wait(1)
        self.play(FadeOut(compEq),FadeOut(cap2))

class NewtonSecondLaw(Scene):
    def construct(self):
        Text1=Tex("La razón de cambio del ", "{momentum}", " con respecto al ", "{tiempo}\\", " de un cuerpo, es igual a la ", "{fuerza resultante}", " que actúa sobre él", font_size=40)
        Text1.set_color_by_tex_to_color_map({
            "{momentum}": carcolor, "{tiempo}":speedcolor,"{fuerza resultante}": dragcolor})
        self.play(Write(Text1))
        self.wait(1.5)
        self.play(ApplyMethod(Text1.to_edge,UP))
        self.wait()

        carheight=1
        carwidth=3
        #Make car
        rectangle = Rectangle(height=carheight, width=carwidth,color=carcolor)
        #rectangle.to_edge(LEFT)
        wheel1=Circle(radius=0.4,color=carcolor)
        wheel2=Circle(radius=0.4,color=carcolor)
        wheel1.move_to(rectangle.get_center()+DOWN*carheight/2+RIGHT)
        wheel2.move_to(rectangle.get_center()+DOWN*carheight/2+LEFT)
        self.play(Create(rectangle),Create(wheel1),Create(wheel2))
        
        
        #Define vectors
        speedlabel=MathTex("\\vec{v}",color=speedcolor)
        draglabel=MathTex("\\vec{F_d}","=-c","\\vec{v}")
        draglabel.set_color_by_tex_to_color_map({
            "{F_d}": dragcolor,
            "{v}":speedcolor})
        
        
    
        speedarrow=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([4,0,0]),color=speedcolor)
        dragarrow=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-4,0,0]),color=dragcolor)
    
        speedlabel.next_to(speedarrow,UP)
        draglabel.next_to(dragarrow,UP)
        
        self.play(Create(speedarrow),Create(dragarrow),Write(speedlabel),Write(draglabel))
        self.wait(1.5)

        speedarrow2=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([6,0,0]),color=speedcolor)
        dragarrow2=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-6,0,0]),color=dragcolor)

        speedarrow3=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([4,0,0]),color=speedcolor)
        dragarrow3=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-4,0,0]),color=dragcolor)


        self.play(Transform(speedarrow,speedarrow2),Transform(dragarrow,dragarrow2))
        self.wait(1.5)
        self.play(Transform(speedarrow,speedarrow3),Transform(dragarrow,dragarrow3))
        self.wait(1.5)
        self.wait(2)
        
        eq1 = MathTex("F &= ma", font_size=70)
        eq1.next_to(rectangle, 4.2*DOWN)
        self.play(Write(eq1))
        self.wait(5)
        eq2 = MathTex("a", "&=", "F","/","m", font_size=70)
        eq2.next_to(rectangle, 4.2*DOWN)
        
        self.play(Transform(eq1, eq2))
        self.wait(7)

        framebox1 = SurroundingRectangle(eq2[0], buff = .1)
        framebox2 = SurroundingRectangle(eq2[2], buff = .1)
        framebox3 = SurroundingRectangle(eq2[4], buff = .1)
        
        self.play(
            Create(framebox1),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(framebox2,framebox3),
        )
        self.wait()

class ExplainNewtonsModel(Scene):
    def construct(self):
        #eq1 = MathTex(r'F &= m * a', font_size=96)
        eq2 = MathTex('a', '&=','\\frac{F}{m}', font_size=96)
        concepts= Tex('Variable\\\\dependiente','Función\\\\fuerza','Propiedad del\\\\sistema')
        self.play(Write(eq2))
        #self.play(ReplacementTransform(eq1,eq2))
        '''for i in range(len(eq2)):
            if i == 0 or i == 2:
                self.play(Indicate(eq2[i]))
                self.wait()'''
        self.play(eq2.animate.shift(5*LEFT))
        self.wait(6.6)        

        carheight=1
        carwidth=3
        #Make car
        rectangle = Rectangle(height=carheight, width=carwidth,color=carcolor)
        #rectangle.to_edge(LEFT)
        wheel1=Circle(radius=0.4,color=carcolor)
        wheel2=Circle(radius=0.4,color=carcolor)
        wheel1.move_to(rectangle.get_center()+DOWN*carheight/2+RIGHT)
        wheel2.move_to(rectangle.get_center()+DOWN*carheight/2+LEFT)
        self.play(Create(rectangle),Create(wheel1),Create(wheel2))
        car = Group(rectangle,wheel1,wheel2)
        speedlabel=MathTex("\\vec{v}",color=speedcolor)
        draglabel=MathTex("\\vec{F}",color=dragcolor)

        speedarrow=Arrow(rectangle.get_center()+np.array([1.5,0,0]),rectangle.get_center()+np.array([3,0,0]),color=speedcolor)
        dragarrow=Arrow(rectangle.get_center()+np.array([-1.5,0,0]),rectangle.get_center()+np.array([-3,0,0]),color=dragcolor)
        
        speedlabel.next_to(speedarrow,UP)
        draglabel.next_to(dragarrow,UP)

        self.play(Create(speedarrow),Create(dragarrow),Write(speedlabel),Write(draglabel))   

        group1 = Group(car, speedlabel, draglabel, speedarrow, dragarrow)
        self.play(group1.animate.scale(0.75).move_to(RIGHT * 3 + 1.5*UP))
        group1_text = Text("Describe un proceso natural", font_size=23, color=YELLOW).next_to(group1, UP)
        self.play(FadeIn(group1_text))
        self.wait(1.9)

        eq3 = eq2.copy()
        self.add(eq3)
        eqr = MathTex("a &= \\pm \\frac{icF\\sqrt{-G^{2}m^{2}+c^{6} t^{2}}}{t\sqrt{-c^{8}m^{2}+F^{2}G^{2}m^{2}-c^{6}F^{2}t^{2}}}", font_size=40, color=speedcolor)
        eqr.to_corner(8*LEFT)
        self.play(
            ReplacementTransform(eq3, eqr),
        )
        group2_text = Text("Es idealizado", font_size=23, color=YELLOW)
        self.play(eqr.animate.scale(0.70).next_to(group1, DOWN, buff=group2_text.height *4))
        group2_text.next_to(eqr, UP)
        self.play(FadeIn(group2_text))
        self.wait(26)
        eq4 = eq2.copy()
        eq5 = MathTex('a &= \\frac{F}{m}', color=speedcolor)
        eq5.next_to(eq2, 2*RIGHT)
        self.play(
            ReplacementTransform(eq4, eq5),
        )
        eqVal = MathTex('a &= \\frac{6N}{2Kg}')
        eqVal.move_to(eq5)
        self.play(
            ReplacementTransform(eq5, eqVal),
        )
        val = MathTex('3','ms^{-2}')
        val.move_to(eqVal)
        self.play(
            ReplacementTransform(eqVal, val),
        )
        group3_text = Text("Resultados reproducibles", font_size=23, color=YELLOW)
        self.play(val.animate.scale(0.70).next_to(eqr, DOWN, buff=group3_text.height *4))
        group3_text.next_to(val, UP)
        self.play(FadeIn(group3_text))
        self.wait(13)
        self.play(Write(eq2))
class IntroductionProblem(Scene):
    def construct(self):
        text = Text("Ejemplo del paracaidista", font_size=60)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text, shift=UP*1.5))
        paratrooper = ImageMobject("paratrooper.png")
        paratrooper.set_height(4)
        fv = Arrow(paratrooper.get_center(
        )+np.array([0, 1.8, 0]), paratrooper.get_center()+np.array([0, 3.2, 0]), color=fvcolor)
        fd = Arrow(paratrooper.get_center(
        )+np.array([0, -1.5, 0]), paratrooper.get_center()+np.array([0, -3, 0]), color=fdcolor)
        fvlabel = MathTex("\\vec{F_{U}}", color=fvcolor)
        fdlabel = MathTex("\\vec{F_{D}", color=fdcolor)
        fvlabel.next_to(fv, RIGHT)
        fdlabel.next_to(fd, RIGHT)
        self.play(FadeIn(paratrooper))
        self.play(Create(fv), Create(fd), Write(fvlabel), Write(fdlabel))
        self.wait(5)


class EquationRate(Scene):
    def construct(self):
        eq = MathTex('a', '&=\\frac{F}{m}', font_size=96)
        acc = MathTex("\\frac{dv}{dt}", font_size=96)
        acc.next_to(eq[1], LEFT)
        self.play(Write(eq))
        self.wait(4)
        self.play(Transform(eq[0], acc))
        self.wait(7)
        framebox1 = SurroundingRectangle(eq[0], buff=.1)
        velocity_text = Tex("Velocidad")
        time_text = Tex("Tiempo")
        velocity_text.next_to(framebox1, UP)
        time_text.next_to(framebox1, DOWN)
        self.play(
            Create(framebox1),
        )
        self.play(FadeIn(velocity_text, shift=UP*0.3))
        self.play(FadeIn(time_text, shift=DOWN*0.3))

class RateFunctions1Example(Scene):
    def construct(self):
        line1 = Line((-3,3,0), (-3,-3,0)).shift(LEFT).set_color(RED)
        line2 = Line((0,3,0), (0,-3,0)).set_color(GREEN)
        line3 = Line((3,3,0), (3,-3,0)).shift(RIGHT).set_color(BLUE)
      
        
        dot1 = Dot().move_to(line1.get_start())
        dot2 = Dot().move_to(line2.get_start())
        dot3 = Dot().move_to(line3.get_start())

        label1 = Tex("F<0").next_to(line1, DOWN)
        label2 = Tex("F>0").next_to(line2, DOWN)
        label3 = Tex("F=0").next_to(line3, DOWN)

        self.play(
            FadeIn(VGroup(line1, line2, line3)),
            FadeIn(VGroup(dot1, dot2, dot3)),
            Write(VGroup(label1, label2, label3)),
        )
        self.wait(2)
        self.play(
            MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
            MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
            MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
            run_time=9
        )
        self.wait()

class ForcesZoom(MovingCameraScene):
    def construct(self):
        paratrooper = ImageMobject("paratrooper.png")
        paratrooper.set_height(4)
        fv = Arrow(paratrooper.get_center(
        )+np.array([0, 1.8, 0]), paratrooper.get_center()+np.array([0, 3.2, 0]), color=fvcolor)
        fd = Arrow(paratrooper.get_center(
        )+np.array([0, -1.5, 0]), paratrooper.get_center()+np.array([0, -3, 0]), color=fdcolor)
        fvlabel = MathTex("F_{U} &= -cv", color=fvcolor)
        fdlabel = MathTex("F_{D} &= m","g", color=fdcolor)
        #gvalue = MathTex("9,81 m/s^{2}")
        #gvalue.next_to(fdlabel[1], DOWN)
        #framebox1 = SurroundingRectangle(fdlabel[1], buff = .1)
        fvlabel.next_to(fv, RIGHT)
        fdlabel.next_to(fd, RIGHT)
        self.play(FadeIn(paratrooper))
        self.wait(7)
        self.play(Create(fd),Write(fdlabel))
        self.wait(5)
        self.play(Create(fv), Write(fvlabel))
        self.wait(5)
        force = MathTex("F &= F_{D} + F_{U}")
        force.next_to(paratrooper)
        self.play(Write(force))
        self.wait(4)
        self.play(self.camera.frame.animate.move_to(fdlabel).set(width=fvlabel.width*2))
        self.wait(15)
        self.play(self.camera.frame.animate.move_to(fvlabel).set(width=fdlabel.width*2))
        self.wait(54)
          
        
class Forces(Scene):
    def construct(self):
        eq1 = MathTex('\\frac{dv}{dt}', '&=','\\frac{\hspace{1.3cm}}{m}', font_size=96)
        f = MathTex("F",font_size=96)
        f1 = MathTex("F_{U}+F_{D}",font_size=96)
        f2 = MathTex("mg-cv",font_size=96)
        f.next_to(eq1[2],UP)
        f1.next_to(eq1[2],UP)
        forces = MathTex("F &= F_{D} + F_{U}")
        forces.next_to(eq1, 1.5*UP)
        self.play(Write(eq1),Write(f), Write(forces))
        self.wait(9)
        self.play(
            ReplacementTransform(f, f1),
            FadeOut(forces)
        )
        self.wait(1)
        f2.next_to(eq1[2],UP)
        self.play(
            ReplacementTransform(f1, f2),
        )
        self.wait(2.6)
        eq = Group(eq1,f2)
        self.play(FadeOut(eq, shift=LEFT*1.5))
        eqsimp = MathTex('\\frac{dv}{dt}', '&= g - \\frac{c}{m}v', font_size=96)
        self.play(Write(eqsimp))
        self.wait(13.2)
        self.play(Wiggle(eqsimp[0]))
        self.wait(25)
        self.play(FadeOut(eqsimp, scale=0.5))
        self.wait(0.6)
        initial_parameters = MathTex("t_{0} = 0", color=BLUE)
        initial_parameters.to_corner(2*UP + 2*LEFT)
        self.play(Write(initial_parameters))
        paratrooper = ImageMobject("paratrooper.png")
        paratrooper.set_height(4.3)
        speedArrow = Arrow(paratrooper.get_center()+np.array([0, -1.5, 0]), paratrooper.get_center()+np.array([0, -3, 0]), color=fdcolor)
        speedlabel = MathTex("V_{0} &= 0", color=fdcolor)
        speedlabel.next_to(speedArrow, RIGHT)
        self.play(FadeIn(paratrooper))
        self.play(Create(speedArrow), Write(speedlabel))
        paratrooper_specifics = Group(paratrooper, speedlabel, speedArrow)
        self.play(paratrooper_specifics.animate.shift(3*LEFT))
        eqsimp.next_to(paratrooper, 2*RIGHT)
        self.play(FadeIn(eqsimp))
        diff_equation = MathTex("v(t) &= \\frac{gm}{c}(1 - e^{(c/m)t})",font_size=70)
        diff_equation.next_to(paratrooper, RIGHT)
        self.wait(13)
        self.play(ReplacementTransform(eqsimp, diff_equation),)
        self.wait(31)
class ProblemDescription(Scene):
    def construct(self):
        description = Tex("\\justifying {Un paracaidista con una masa de 68.1 kg salta de un globo aerostático fijo, considerando que el coeficiente de resistencia es igual a 12.5 kg/s}")
        description.scale(0.7)
        self.play(Write(description))
        self.wait(19)
        self.play(FadeOut(description))

class AnaliticalSolution(Scene):
    def construct(self):
        diff_equation = MathTex("v(t) &=", "\\frac{\hspace{1.5cm}}{\hspace{1.5cm}}","(1 -", "e",font_size=70)
        num = MathTex("g","m",font_size=70)
        den = MathTex("c",font_size=70)
        exp1 = MathTex("-(","c",font_size=40)
        exp2 = MathTex("/","m",font_size=40)
        exp3 = MathTex("t)",font_size=40)
        par = MathTex(")",font_size=70)

        num.next_to(diff_equation[1], UP)
        den.next_to(diff_equation[1], DOWN)
        exp1.next_to(diff_equation[3],1.5*RIGHT+0.01*UP)
        exp2.next_to(exp1, 0.1*RIGHT)
        exp3.next_to(exp2, 0.1*RIGHT)
        par.next_to(diff_equation[3], 8*RIGHT)
        equation1 = Group(diff_equation, num, den, exp1, exp2,exp2,exp3, par)
        diff_equation.arrange(2*RIGHT)
        self.play(Write(diff_equation),Write(num),Write(den),Write(exp1),Write(exp2), Write(exp3),Write(par))
        self.play(equation1.animate.scale(0.75).move_to(UP * 2.5))

        g = MathTex("g =","9.8", font_size=70)
        m = MathTex("m =","68.1",font_size=70)
        c = MathTex("c =","12.5",font_size=70)
        m3 = MathTex("68.1", font_size=30)
        c3 = MathTex("12.5", font_size=30)
        self.play(FadeIn(g))
        self.play(
            FadeOut(num[0]),
            FadeOut(g[0]),
            g[1].animate.scale(0.75).move_to(num[0].get_center()+np.array([-0.4,0,0])),
            num[1].animate.shift(0.1*RIGHT+0.1*DOWN)
        )
        simb = MathTex("*")
        simb.next_to(g[1],0.5*RIGHT)
        self.play(FadeIn(simb))
        self.play(FadeIn(m))
        
        
        m3.next_to(exp1,RIGHT)
        self.play(
            FadeOut(num[1]),
            FadeOut(m[0]),
            FadeOut(exp2[1]),
            FadeIn(m3),
            m[1].animate.scale(0.75).move_to(num[0].get_center()+np.array([0.8,0,0])),
            exp3.animate.shift(0.6*RIGHT),
            par.animate.shift(0.6*RIGHT)  
        )
        simbsub = MathTex("*",font_size=30)
        simbsub.next_to(m3,0.4*RIGHT)
        self.play(FadeIn(simbsub))
        
        self.play(FadeIn(c))
        c3.next_to(exp1[0],0.1*RIGHT)
        group = Group(par, simbsub, exp3, exp2[0], m3 )
        self.play(
            FadeOut(den),
            FadeOut(c[0]),
            group.animate.shift(0.4*RIGHT),
            FadeOut(exp1[1]),
            FadeIn(c3),
            c[1].animate.scale(0.75).move_to(den.get_center()),
        )
        #final_expression = MathTex("v(t) &= 53.39(1-e^{0.18355t})")
        final_expression = MathTex("v(","t\hspace{0.2cm}",")&=", "53.39(1-e")
        exp = MathTex("-0.18355", font_size=30)
        exptime = MathTex("t",font_size=30)
        exppar = MathTex(")")
        exp.next_to(final_expression,0.1*RIGHT+0.01*UP)
        exptime.next_to(exp, 0.2*RIGHT)
        exppar.next_to(final_expression, 6*RIGHT)
        final_function = Group(final_expression, exp, exptime, exppar)
        final_function.shift(UP * 2.5)
        equation_value = Group(diff_equation, exp1[0], exp2[0], exp3, par, g[1], m[1], c[1], m3, c3, simb, simbsub )
        self.play(
            ReplacementTransform(equation_value, final_function),
        )
        

        #Tabla
        table = Table(
            [["t[s]", "v[m/s]"]]).scale(0.6)
        table.shift(UP*1.2)
        lineh = Line(table.get_center()+np.array([-2.2, -0.4, 0]),table.get_center()+np.array([2.2, -0.4, 0]))
        linev = Line(table.get_center()+np.array([-0.26, -0.4, 0]),table.get_center()+np.array([-0.26, -5, 0]))
        self.play(table.create())   
        self.add(lineh)
        self.add(linev)

        '''ran = Tex("asd", color=BLACK)
        ran.shift(table.get_center()+np.array([-1, -1, 0]))
        self.add(ran)'''

        
        timeInput = MathTex("0","2","4","6","8","10","12")
        timeData = MathTex(" *0"," *2"," *4"," *6"," *8"," *10"," *12", font_size=30)
        speedData = MathTex("0.00","16.40","27.77","35.64","41.10","44.87","47.49")
        self.play(FadeOut(exptime),FadeOut(final_expression[1]), final_function.animate.shift(LEFT))
        self.play(exppar.animate.shift(0.5*RIGHT))
        

        t = -0.8
        eqsimb = MathTex("=")
        eqsimb.next_to(exppar, 0.5*RIGHT)
        self.play(FadeIn(eqsimb))
        for i in range(len(timeData)):
            if i==5:
                groupExp = Group(final_expression[2],final_expression[3],exp,exppar,eqsimb )
                self.play(groupExp.animate.shift(0.2*RIGHT))
            timeData[i].next_to(exp, 0.5*RIGHT)
            timeInput[i].next_to(final_expression[0], 0.5*RIGHT)
            speedData[i].next_to(eqsimb,0.5*RIGHT)
            self.play(
                FadeIn(timeData[i]),
                FadeIn(timeInput[i]),
                FadeIn(speedData[i])
            )
          
                
            self.wait()
            if i == 0:
                self.play(timeInput[i].animate.scale(0.8).move_to(table.get_center()+np.array([-1, -0.8, 0])), speedData[i].animate.scale(0.8).move_to(table.get_center()+np.array([1, -0.8, 0])),FadeOut(timeData[i]) )
            else:
                t -=0.5
                self.play(timeInput[i].animate.scale(0.8).move_to(table.get_center()+np.array([-1, t, 0])),speedData[i].animate.scale(0.8).move_to(table.get_center()+np.array([1, t, 0])),FadeOut(timeData[i]))     
        infsimb = MathTex("\infty")
        speedDataVal = MathTex("53.39")
        self.play(infsimb.animate.scale(0.8).move_to(table.get_center()+np.array([-1, t-0.5, 0])), speedDataVal.animate.scale(0.8).move_to(table.get_center()+np.array([1, t-0.5, 0])),FadeOut(timeData[i]) )
        self.wait(120)

class AnliticalSolutionGraph(Scene):
    def construct(self):
        title = Tex("Gráfica de la solución analítica")
        ax = Axes(
            x_range=[0,60,10],
            y_range=[0,100,20],
            #x_axis_config={"numbers_to_include": np.arange(0,14,2)},
            #y_axis_config={"numbers_to_include": np.arange(0,60,10)},
            tips=False,
        )
        labels = ax.get_axis_labels(x_label="v[m/s]", y_label="t[s]")
        def func(x):
            return 87.16*tanh(0.112*x)
        graph = ax.plot(func, color=MAROON)
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        title.shift(3.2*UP)
        
        self.add(ax, labels, moving_dot, graph)
        self.play( Write(title))
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.wait(14) 


class AnaliticalSolutionExplain(Scene):
    def construct(self):
        solution = MathTex("\\frac{dv}{dt} &= g - \\frac{c}{m}v", font_size=70)
        text = Tex("Solución analítica", color=YELLOW, font_size=70)
        text.shift(2.5*UP)
        self.play(Write(text), Write(solution))
        self.wait(60)

class NumericalEqualitySolution(Scene):
    def construct(self):
        text = Text("Métodos numéricos", font_size=60, color=BLUE)
        self.play(Write(text))
        self.play(text.animate.shift(UP*2))
        eq0 = MathTex("\\frac{dv}{dt}","&= \\frac{v(t_{i+1}) - v(t_{i})}{t_{i+1} - t_{i}}", font_size=70)
        delta = MathTex("\cong \\frac{\Delta v}{\Delta t} ", font_size=70)
        self.play(Write(eq0))
        delta.next_to(eq0[0], 0.5*RIGHT)
        self.wait(15.2)
        self.play(eq0[1].animate.shift(1.8*RIGHT))
        self.play(FadeIn(delta))
        self.wait(55.2)

'''class Aproximations(Scene):
    def construct(self):
        diff = MathTex("\\frac{dv}{dt}","\cong \\frac{\Delta v}{\Delta t} ")
        self.play(Write(diff))
        limit = MathTex("&= \lim_{\Delta t\to\ 0} \\frac{\Delta v}{\Delta t} ")
        limit.next_to(diff[0], 0.5*RIGHT)
        self.play(ReplacementTransform(diff[1],limit))'''

class NumericalEquation(Scene):
    def construct(self):
        eqDiff = MathTex("\\frac{dv}{dt}", "&= g - \\frac{c}{m}v")
        diff = MathTex("\\frac{dv}{dt}\cong \\frac{\Delta v}{\Delta t} &=","\\frac{v(t_{i+1}) - v(t_{i})}{t_{i+1} - t_{i}}" )
        diff.next_to(eqDiff, DOWN)
        self.play(Write(eqDiff))
        self.play(eqDiff.animate.scale(1).shift(UP))
        self.play(Write(diff))
        self.play(
            FadeOut(diff[0]),
            FadeOut(eqDiff[0]),
            eqDiff[1].animate.shift(RIGHT+DOWN),
            diff[1].animate.next_to(eqDiff[1],0.1*LEFT+0.3*DOWN)
            
            
        )
        self.play(diff[1].animate.next_to(eqDiff[1],LEFT))
        
        self.wait(15.2)

class finalEquation(Scene):
    def construct(self):
        eqDiff = MathTex("\\frac{dv}{dt}&=", "g - \\frac{c}{m}v")
        finalEq = MathTex("v(t_{i+1}) &= v(t_{i}) +", "[g - \\frac{c}{m}v(t_{i})]","(t_{i+1}-t_{i})")
        self.play(Write(finalEq))
        self.play(finalEq.animate.scale(1).shift(UP))
        eqDiff.next_to(finalEq, 1.3*DOWN)
        self.play(Write(eqDiff))

        framebox1 = SurroundingRectangle(eqDiff[1], buff = .1)
        framebox2 = SurroundingRectangle(finalEq[1], buff = .1)
        self.play(
            Create(framebox1),
            Create(framebox2)
        )
        self.play(
            FadeOut(framebox1), FadeOut(framebox2), FadeOut(eqDiff)
        )
     
        exp = Tex("valor nuevo = valor anterior + pediente * tamaño del paso")
       
        exp.next_to(finalEq, DOWN)
        self.play(Write(exp))
        name = Tex("Método de Euler", font_size=60, color=YELLOW)
        name.shift(UP*2.5)
        self.play(Write(name))
        self.wait(30)
class appliedEquation(Scene):
    def construct(self):
        table = Table(
            [["t[s]", "v[m/s]"],
            ["0", "0.00"],
            ["2", "19.60"],
            ["4", "32.00"],
            ["6", "39.85"],
            ["8", "44.82"],
            ["10", "47.97"],
            ["12", "49.96"],
            ["∞", "53.39"],
        ]).scale(0.5)
        self.play(table.create())
        finalEq = MathTex("v(t_{i+1}) &= v(t_{i}) +", "[g - \\frac{c}{m}v(t_{i})]","(t_{i+1}-t_{i})",font_size=35)
        finalEq.shift(LEFT)
        self.play(table.animate.shift(2*RIGHT),
            finalEq.animate.shift(2*LEFT)
        )
        framebox1 = SurroundingRectangle(finalEq, buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait(60)
                   
        
        



