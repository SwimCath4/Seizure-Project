function [ instance ] = spectral_entropy(data)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

% Process the data
[num_data_pts, ~] = size(data);

% The following routine is based off of information found on Stack Exchange
% 1. Calculate frequency spectrum using fast fourier transform
fourier = fft(data);

% 2. Calculate the Power Spectral Density
P = abs(fourier).^2 / num_data_pts;

% 3. Convert the PSD into a probability density function (PDF)
p = P./repmat(sum(P), num_data_pts, 1);

% 4. Compute entropies. Each value corresponds to the channel's entropy    
instance = -sum(p .* log(p)) / num_data_pts;
end

