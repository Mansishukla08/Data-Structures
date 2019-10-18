#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node* link;
};

struct node* head;

int len(){
	int count=0;
	struct node* temp=head;
	while(temp!=NULL){
		count++;
		temp=temp->link;
	}
	return count;	
}

void print(){
	struct node* temp=head;
	printf("The Linked list is follows: \n");
	while(temp!=NULL){
		printf("%d\t",temp->data);
		temp=temp->link;
	}
}

void addFirst(int data){
	struct node* temp=(struct node*)malloc(sizeof(struct node));
	temp->data=data;
	temp->link=head;
	head=temp;
}
void addLast(int data){
	struct node* temp=head;
	struct node* new=(struct node*)malloc(sizeof(struct node));
	new->data=data;
	if(temp==NULL){
		new->link=head;
		head=new;
	}else{
		while(temp->link!=NULL){
			temp=temp->link;
		}
		new->link=temp->link;
		temp->link=new;
	}
}
void add(int data,int loc){
	struct node* temp=head;
	struct node* new=(struct node*)malloc(sizeof(struct node));
	new->data=data;
	if(loc==0){
		new->link=head;
		head=new;
	}else{
		for(int i=0;i<loc-1;i++){
			temp=temp->link;
		}
		new->link=temp->link;
		temp->link=new;
	}
}
void deleteLast(){
	struct node* temp=head;
	struct node* tail=head;
	while(temp->link!=NULL){
		temp=temp->link;
	}
	while(tail->link!=temp){
		tail=tail->link;
	}
	tail->link=NULL;
	free(temp);

}
