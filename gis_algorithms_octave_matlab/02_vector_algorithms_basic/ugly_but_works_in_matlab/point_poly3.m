% ************************************************************%%           point_poly.m%%       %   Author:%   Date:%% ************************************************************%clear, clfformat short%Loading in Polygons and Coordinates dataload Polygons.txtload Coord.txt%Storing ncol and nrow[ncol, nrow] = size(Polygons);%Init plot in bluehold on;for i=1:ncol  including_zeros = Polygons(i,:);  pol_index_array = [] ;  for j=1:length(Polygons(i,:))    if Polygons(i,j) ~= 0      pol_index_array(j) = including_zeros(j);    end %if  end %for  x = transpose(Coord(pol_index_array,1));  y = transpose(Coord(pol_index_array,2));  plot(x,y, 'b-');end%Set control structure variablecontinue_prog = 1;while continue_prog == 1  %Display message to user  disp("Click in an arbitrary polygon:");  %Setting coordinates from click  [click_x, click_y] = ginput(1);  p_click = [click_x, click_y];  %Initializing "Support point" outside of plot area, same height as y-click  p_sup = [0, click_y]; %x=0, y=click  for i=1:ncol %For each polygon    including_zeros = Polygons(i,:);    pol_index_array = [] ;    for j=1:length(Polygons(i,:))      if Polygons(i,j) ~= 0        pol_index_array(j) = including_zeros(j);      end %if    end %for    x = transpose(Coord(pol_index_array,1)); %Get x     y = transpose(Coord(pol_index_array,2)); %and y coord from index    sum_inside = 0; %initialize sum    for j=1:length(x)-1 %For each line segment      %Check condition      if (side_triangle([x(j), y(j)], [x(j+1), y(j+1)], p_click) ~= (side_triangle([x(j), y(j)], [x(j+1), y(j+1)], p_sup))) && (side_triangle(p_click, p_sup,[x(j), y(j)]) ~= (side_triangle(p_click, p_sup,[x(j+1), y(j+1)])))        sum_inside = sum_inside + 1; %If condition valid, add one to sum      end; %if    end; %for    if mod(sum_inside,2) == 1 %Check sum for current polygon, if not divisible by 2 (i.e. 0 or 2)      index_inside = i; %Then this is the clicked polygon      break    end %if  end; %for  %Extract and plot clicked polygon in red  including_zeros = Polygons(index_inside,:);  pol_index_array = [] ;  for j=1:length(Polygons(i,:))    if Polygons(i,j) ~= 0      pol_index_array(j) = including_zeros(j);    end %if  end %for  x = transpose(Coord(pol_index_array,1));  y = transpose(Coord(pol_index_array,2));  plot(x,y, 'r-');    %Luckily all sorted, but in counter-clockwise direction... so need to negate area calc.  %also, here have start point listed twice, where my area_pol()  %Function assumed only once.  %However, data set up so that these points are vertical, i.e. area=0  %But for a bit more generalizability, instead of:  %-area_pol([transpose(x),transpose(y)])  area_selected = -area_pol([transpose(x(1:length(x)-1)),transpose(y(1:length(y)-1))]);  %Display selected polygon and area  disp("The number of the selected polygon is:");  disp(index_inside);  disp("The area of the polygon is (square meter):");  disp(area_selected);  %Let user set control structure variable  continue_prog = input("Press 1 (=continue to select polygons) or 0 (=stop the program):")end %while