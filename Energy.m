function feat = Energy(X) 
[m,n] = size(X);
feat = sum(X.^2)/m;

end