% ************************************************************
%
%           E8.m
%
%       
%   Author: Jonas Tillman
%   Date: 2017-04-09
%
% ************************************************************
%
clear, clf
format short
%
% Draw the map.
load coord3.txt;
nrow = size(coord3)(1);

alphabet = 'abcdefghijkl'
hold on;
for i=1:nrow
  %letter =  strcat("'", alphabet(i), "'")
  letter =  alphabet(i)
  text(coord3(i,1)+7,coord3(i,2), letter),hold on;
  plot(coord3(i,1),coord3(i,2), '.'),hold on;
end;


%hold on;
%for i=1:nrow
%  plot(coord3(i,1),coord3(i,2), 'o');
%end;



axis([0 1000 0 1000]);

morton_array = zeros(nrow,1);

for i=1:nrow
  morton_array(i) = morton(coord3(i,1),coord3(i,2));
end

morton_array

%  End
%  