#include<iostream>
using namespace std;
class A //基类A
{
   protected:
      int a;
      public:
      int Set(int i) //给数据成员a赋值
      {
         i = a;
      }
      int Get() //返回数据成员a的值
      {
         return a;
      }
};
class B:public A//从A类公有派生B类
{
   protected:
      int b;
      public:
      int Set_1(int i) //给数据成员b赋值
      {
         i = b;
      }
      int Get_1() //返回数据成员b的值
      {
         return b;
      }
      void Show_1() //输出数据成员a和b的值
      {
         cout << "A::a=" << a << ", B::b=" << b << endl;
      }
};
int main()
{
   B bb; //创建类B的对象bb
   int x, y;
   cin >> x >> y;
   bb.Set_1(x); //给数据成员a赋值
   bb.Set_1(y); //给数据成员b赋值
   bb.Show_1();
   return 0;
}
