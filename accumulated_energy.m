function [ acc_energy ] = accumulated_energy(X)

%% Define width and shift values for accumulated energy calculation %%
width = 10;
shift = 5;

%% Compute first energy calculation %%

E_k = Energy(X(1:width,:)) ./ width;
acc_energy = E_k;
num_data_pts = length(X);

%% Calculate m - number of times to update accumulated energy %%
% Handle case in which number of instances is not divisible by shift # %

m = floor((num_data_pts-(width) + (shift))/(shift));

%% Output a vector of accumulated eneries. Each value corresponds to the channel's energy %%

for i=2:m
    acc_energy = acc_energy + (Energy(X(i*shift:i*shift + width)) ./ width);

acc_energy = acc_energy / m;
