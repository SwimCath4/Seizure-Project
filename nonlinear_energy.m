
function nonlin_e = nonlinear_energy(data)

num_data_pts = size(data)(1);
number_of_channels = size(data)(2);
nonlin_e = zeros([number_of_channels, 1]); % initialize final array

% Output a vector of eneries. Each value corresponds to the channel's energy
for channel = 1:number_of_channels
  for i = 2:(num_data_pts - 1)	% START WITH THE SECOND DATA POINT
		nonlin_e(channel, 1) = nonlin_e + X(i, channel)^2 - (X(i - 1, channel) * X(i + 1, channel));
  end
end