% ************************************************************
%
%           dijkstra.m
%
%   The program computes the shortest path in a network
%   using Dijkstra's algorithm.
%
%   The example and the Algorithm is taken from 
%   Worboys, M. F., and M. Duckham, 2004. 
%   GIS: A Computing Perspective, 2nd edition. Taylor & Francis.
%   Pages: 214-217
%       
%   Author: Jonas Tillman
%   Date: 2017-04-09
%
% ************************************************************
%
clear, clf
format short
%
% Specify the number of Vertices in the network  
Vertices=8;
%
% Create the adjacency matrix
Adj_Matrix=[ 0 20  0  0  0  0 15  0 ; ...
	    20  0  8  9  0  0  0  0 ; ...
             0  8  0  6 15  0  0 10 ; ... 
	     0  9  6  0  7  0  0  0 ; ...
             0  0 15  7  0 22 18  0 ; ...
             0  0  0  0 22  0  0  0 ; ...
            15  0  0  0 18  0  0  0 ; ...
             0  0 10  0  0  0  0  0 ];
%
% Create the state matrix
State_Matrix=[ Inf 0  0 ; ...
	       Inf 0  0 ; ...
	       Inf 0  0 ; ...
	       Inf 0  0 ; ...
	       Inf 0  0 ; ...
	       Inf 0  0 ; ...
	       Inf 0  0 ; ...
	       Inf 0  0 ]; 
%
% Define the coordinates of the vertices. Be aware of that
% these coordinates are only used for presentation purposes.
% All distances in the computations are based on the 
% adjacency matrix.
Coord_Matrix=[ 0 5 ; 1 0 ; 5 1 ; 2 4 ; 3 6 ; 0 7 ; 4 8 ; 6 2 ];
%
% Draw the network.
text(Coord_Matrix(1,1), Coord_Matrix(1,2), '1'),hold on
text(Coord_Matrix(2,1), Coord_Matrix(2,2), '2'),hold on
text(Coord_Matrix(3,1), Coord_Matrix(3,2), '3'),hold on
text(Coord_Matrix(4,1), Coord_Matrix(4,2), '4'),hold on
text(Coord_Matrix(5,1), Coord_Matrix(5,2), '5'),hold on
text(Coord_Matrix(6,1), Coord_Matrix(6,2), '6'),hold on
text(Coord_Matrix(7,1), Coord_Matrix(7,2), '7'),hold on
text(Coord_Matrix(8,1), Coord_Matrix(8,2), '8'),hold on
%
for i=1:Vertices
	for j=1:(i-1)
		if Adj_Matrix(i,j)~=0
			Graphx=[Coord_Matrix(i,1) Coord_Matrix(j,1)];
			Graphy=[Coord_Matrix(i,2) Coord_Matrix(j,2)];
			plot(Graphx,Graphy,':'),hold on
		end;
	end;
end;
%
axis('equal');
axis('off');
%
% Specify the start and end point for the search
startPoint=input('Give the start point (integer):  ');
endPoint=input('Give the end point (integer):  ');
%
% Here you should add the shortest path computations
% according to Dijkstra's algorithm.
%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Initialize State Matrix [Distance, Path, Visited]
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
cur_node = startPoint;
[state_nrows, state_ncol] = size(State_Matrix);
[adj_nrows, adj_ncol] = size(Adj_Matrix);
%The start node is marked as visited, and distance from start point to 0.
State_Matrix(startPoint,3) = 1; %visited
State_Matrix(startPoint,2) = startPoint; %path
State_Matrix(startPoint,1) = Adj_Matrix(startPoint,startPoint); %distance

%All nodes that can be reached from the start node are updated (distance and path) 
for i=1:adj_ncol
  if (Adj_Matrix(startPoint,i) ~= 0)
    %Distance
    State_Matrix(i,1) = Adj_Matrix(startPoint,i);
    %Path
    State_Matrix(i,2) = startPoint; 
  end
end    

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Main work of algorithm
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


while (cur_node ~= endPoint)
  select_adj_matrix = Adj_Matrix(cur_node,:); %cur_adj_matrix_row
  state_mat_unvisit = State_Matrix(:,3)==0; %for filtering
  for_min_dist = state_mat_unvisit .* transpose(select_adj_matrix); %only keeping the unvisited distances
  if (max(for_min_dist) == 0) %if from the node there are no unvisited nodes...
  %This if statement was added due to that the algorithm failed if
  %a end-node wasn't visited initially, This is a bit of a ugly
  %hack, but since I initially didn't know this would be an issue,
  %this is a work-around for thsoe corner cases...
    [x,not_visited] = max((State_Matrix(:,3) == 0));  %finding the first unvisited
    [x,cur_node] = max(Adj_Matrix(not_visited,:));
  else
    min_dist = min(for_min_dist(for_min_dist>0)); %select min dist.
    %marking shortest distance not visited as cur_node
    [x,cur_node] = max((Adj_Matrix(cur_node,:) == min_dist)); 
    %setting as visited
    State_Matrix(cur_node,3) = 1;
  end; %if
  
  for i=1:adj_ncol
    if (State_Matrix(i,3) == 0 && Adj_Matrix(cur_node,i)~=0) %only unvisited AND they are connected
      temp_sum = State_Matrix(cur_node,1) + Adj_Matrix(cur_node,i);
      if (temp_sum<State_Matrix(i,1)) %if current explored distance less, do nothing, otherwise:
        State_Matrix(i,1) = temp_sum; %update distance
        State_Matrix(i,2) = cur_node; %update path
      end %if
    end %if
  end %for
end %while



tot_dist = State_Matrix(endPoint,1); %total distance
%Update total shortest path
for_path_frontier = endPoint;
path_shortest = [endPoint];
while (for_path_frontier ~= startPoint);
  for_path_frontier = State_Matrix(for_path_frontier,2);
  path_shortest = [path_shortest,for_path_frontier];
end;

%PRINT RESULTS
disp(sprintf('The shortest distance from %u to %u is %u',startPoint,endPoint,tot_dist))
path_shortest = flip(path_shortest);
disp("The shortest path is:")
disp(path_shortest)



%%%%%%%%DRAW
%UNLEAR IF JUST PRINTING TO WINDOW IS ENOUGH, OR IF NEEDED TO PLOT THAT AS WELL?
% Draw the network.
%startPoint
%text(Coord_Matrix(startPoint,1), Coord_Matrix(startPoint,2), 'Start'),hold on
%text(Coord_Matrix(endPoint,1), Coord_Matrix(endPoint,2), 'End'),hold on
%for i=2:path_shortest
%  text(Coord_Matrix(i,1), Coord_Matrix(i,2), num2str(i)),hold on
%end;



%  End
%  