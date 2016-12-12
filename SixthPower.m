function feat = SpectralEntropy(X) 
[m,n] = size(X);
feat = sum(X.^6)/m;

end