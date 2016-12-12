function [ acc_energy ] = accumulated_energy(X)

%% Define width and shift values for accumulated energy calculation %%
width = 2;
shift = 1;

%% Compute first energy calculation %%

E_k = Energy(X(1:width,:)) ./ width;
acc_energy = E_k;
[num_data_pts, ~] = size(X);

%% Calculate m - number of times to update accumulated energy %%
% Handle case in which number of instances is not divisible by shift # %

m = floor((num_data_pts-(width) + (shift))/(shift));

%% Output a vector of accumulated eneries. Each value corresponds to the channel's energy %%

for i=1:m-1
    %disp(X(i*shift+1:(i*shift + width),:))
    acc_energy = acc_energy + (Energy(X(i*shift+1:(i*shift + width),:)) ./ width);
end

acc_energy = acc_energy ./ m;
