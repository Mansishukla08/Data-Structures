#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node* link;
};

struct node* head;

void print(){
	struct node* temp=head;
	printf("The queue is follows: \n");
	while(temp!=NULL){
		printf("%d\t",temp->data);
		temp=temp->link;
	}
}

void enqueue(int data){
	struct node* temp=(struct node*)malloc(sizeof(struct node));
	temp->data=data;
	temp->link=head;
	head=temp;
}
void dequeue(){
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
