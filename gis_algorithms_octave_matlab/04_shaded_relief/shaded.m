% ************************************************************
%
%           shaded.m
%
%       
%   Author: Jonas Tillman
%   Date: 2017-04-16
%
% ************************************************************
%
clear
format short
pkg load image
#Load DEM
load DEM.txt;

#ALLOW FOR USER INPUT, pos of sun, convert to radians
prompt = 'What is the height angle of the sun (in degrees) from the earth surface? [num + enter]';
alpha_inp = input(prompt) * pi/180;
prompt = 'What is the clockwise position of the sun from the north (in degrees)? [num + enter]';
beta_inp = input(prompt) * pi/180;
#alpha_inp =45; #HEIGHT ANGLE 
#beta_inp =315; #CLOCLWISE FROM NORTH SUN POSITION, DEGREES

#Defining resolution
d_y = 50;
d_x = 50;
#Setting up sobel filters, x- and y-direction
y_dir_sobel = [1 2 1; 0 0 0; -1 -2 -1];
x_dir_sobel = [-1 0 1; -2 0 2; -1 0 1];

#Getting nrows and ncolumns from the DEM
[nrow, ncol]= size(DEM);

#Loop over and get first y- and then x-direction sobel filter (correlation) results
y_sob_res = zeros(nrow-2,ncol-2);
for i=1:nrow-2
  for j=1:ncol-2
    y_sob_res(i,j) = (1/(8*d_y))*sum(sum(DEM(i:i+2,j:j+2).* y_dir_sobel));
  end
end

x_sob_res = zeros(nrow-2,ncol-2);
for i=1:nrow-2
  for j=1:ncol-2
    x_sob_res(i,j) = (1/(8*d_y))*sum(sum(DEM(i:i+2,j:j+2).* x_dir_sobel));
  end
end

#Set a and b to default values
a = 0;
b = (1/sqrt(2));

#Set p_0 and q_0
p_0 = -cos(beta_inp)*tan(alpha_inp);
q_0 = -sin(beta_inp)*tan(alpha_inp);

#Combined p eval results
p_comb = (p_0*x_sob_res + q_0*y_sob_res)/sqrt(p_0^2 + q_0^2);

#Get shaded relief output according to formula
shade_matrix = 0.5 + 0.5*(p_comb+a)/b;

%3D graph
%surf(shade_matrix)

#Surface output plot
surface(shade_matrix)
colormap(gray); 

#image(imfilter(DEM, fspecial("sobel")))
#image(imfilter(y_sob_res, fspecial("sobel")))
