import graphene
import questions.schema 

class Query(questions.schema.Query, graphene.ObjectType):
        # This class extends all abstract apps level Queries and graphene.ObjectType
        pass    

class Mutation(questions.schema.MyMutations, graphene.ObjectType):  
        # This class extends all abstract apps level Mutations and graphene.ObjectType
     pass

schema = graphene.Schema(query=Query,mutation= Mutation)













#query=Query
#questions.schema.Query,
