#include<iostream>
using namespace std;
class A //����A
{
   protected:
      int a;
      public:
      int Set(int i) //�����ݳ�Աa��ֵ
      {
         i = a;
      }
      int Get() //�������ݳ�Աa��ֵ
      {
         return a;
      }
};
class B:public A//��A�๫������B��
{
   protected:
      int b;
      public:
      int Set_1(int i) //�����ݳ�Աb��ֵ
      {
         i = b;
      }
      int Get_1() //�������ݳ�Աb��ֵ
      {
         return b;
      }
      void Show_1() //������ݳ�Աa��b��ֵ
      {
         cout << "A::a=" << a << ", B::b=" << b << endl;
      }
};
int main()
{
   B bb; //������B�Ķ���bb
   int x, y;
   cin >> x >> y;
   bb.Set_1(x); //�����ݳ�Աa��ֵ
   bb.Set_1(y); //�����ݳ�Աb��ֵ
   bb.Show_1();
   return 0;
}
