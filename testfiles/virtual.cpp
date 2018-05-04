#include
using namespace std;
uditt // usd

/*udf
fddg
sa
as*/




class b
{
    public:
    virtual void show() // jisdcf
    {
        cout<<"\n  Showing base class....";
    }
    void display()
    {
        cout<<"\n  Displaying base class...." ;
    }
};

class d:public b
{
    public:
    void display()
    {
        cout<<"\n  Displaying derived class....";
    }
    void show()
    {
        cout<<"\n  Showing derived class....";
    }
};

int main()
{
    b B;
    b *ptr;
    cout<<"\n\t P points to base:\n" ; ptr=&B; ptr->display();
    ptr->show();
    cout<<"\n\n\t P points to drive:\n"; d D; ptr=&D; ptr->display();
    ptr->show();
}
