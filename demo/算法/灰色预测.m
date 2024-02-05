clc, clear
x0=[34,45,78,90];
n=length(x0);
x1=zeros(1,n);
x1(1)=x0(1);
for i=2:n
    x1(i)=x0(i)+x1(i-1);
end
af=0.4;
z1=zeros(1,n);
z1(1)=0;
for i=2:n
    z1(i)=x1(i)*af+(1-af)*x1(i-1);
end
Y=zeros(n-1,1);
X=zeros(n-1,2);
for i=2:n
    Y(i-1)=x0(i);
    X(i-1)=-z1(i);
    X(i-1,2)=1;
end
B=inv(X'*X)*X'*Y;
a=B(1);
b=B(2);
pred_n_1=(x0(1)-b/a)*exp(-a*n)*(1-exp(a));
x=0:0.1:4;
y3=(x0(1)-b/a).*exp(-a.*x).*(1-exp(a))
plot(x, y3,'*')
hold on
n0=0:3;
plot(n0,x0,'ro')