%% Viper s850 parameters %%

%DH parameters

l1=203; %mm
l2=[75 0 130]; %mm
l3=365,15; %mm
l4=[0 -89.66 218] ; %mm
l5=[0 187 0]; %mm
l6=51.8; %mm
endPlate=40; %mm
endTor=[-100, 0 0]; %mm
%Joints Limits in deg

j1=170;
j2u=45;
j2d=-190;
j3u=259;
j3d=-29;
j4=190;
j5=120;

viper=importrobot('Vipers850.slx')
