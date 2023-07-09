import heapq

def rank_people(N, P, ranked_weights, unranked_weights):
    
    # Sort the ranked and unranked weights in the required order
    ranked_weights.sort(reverse=True)
    unranked_weights.sort()

    # Initialize the priority queue and next rank
    pq = []
    next_rank = N + 1

    # Insert the ranked people into the priority queue
    for weight in ranked_weights:
        heapq.heappush(pq, (weight, next_rank))
        next_rank -= 1

    # Rank the unranked people and print their ranks
    for weight in unranked_weights:
        heapq.heappush(pq, (weight, next_rank))
        print(next_rank)
        next_rank -= 1

N, P = map(int, input().split())
ranked_weights = list(map(int, input().split()))
unranked_weights = list(map(int, input().split()))

# Call the rank_people function
rank_people(N, P, ranked_weights, unranked_weights)
