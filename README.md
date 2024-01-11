# Modelling-and-Analysis-of-Traffic-Flows

<div id="header" align="center">
  <img src="https://media.giphy.com/media/Y349mkUUL76bwZHlJR/giphy.gif"/>
</div>

Many researchers have described the nature of traffic flows using partial differential
equations (PDE’s) and ordinary differential equations (ODE’s). Most of them use
the concept of the conservation laws in fluid mechanics. For example, the model
introduced by Lighthill-Whitman-Richards (LWR Model) is formulated as a nonlinear
partial differential equation, derived by using the conservation of vehicles on a single
road. This project describes the nature of traffic flow using a three-
dimensional nonlinear dynamical system called the FBDF model. 
The well posedness of the model was established and the local stability analysis of the
equilibrium points has been carried out using the retardation number while the
global stability analysis has been performed using LaSalle’s invariance principle.
The numerical simulations were carried out using Python. Furthermore
the sensitivity analysis of the parameters has been performed via two methods: a derivative-based local
method and algorithmic differentiation. 
