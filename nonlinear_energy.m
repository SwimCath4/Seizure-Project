
function nonlin_e = nonlinear_energy(data)
[num_data_pts, number_of_channels] = size(data);
nonlin_e = zeros([1, number_of_channels]); % initialize final array

% Output a vector of eneries. Each value corresponds to the channel's energy
for channel = 1:number_of_channels
  for i = 2:(num_data_pts - 1)	% START WITH THE SECOND DATA POINT
		nonlin_e(1, channel) = nonlin_e(1, channel) + data(i, channel)^2 - (data(i - 1, channel) * data(i + 1, channel));
  end
end