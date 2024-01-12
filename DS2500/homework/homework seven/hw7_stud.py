#!/usr/bin/env python
# coding: utf-8

# # DS 2500 HW 7

# In[1]:


from copy import copy
import pandas as pd

class BayesNetwork:
    """ bayes net, computes full joint table

    Attributes:
        df_joint (pd.DataFrame): a column per random variable plus another col
            for probability.  each row contains the outcomes of the
            corresponding random variable or the joint prob of entire row
    """
    def __init__(self):
        self.df_joint = pd.DataFrame({"prob": [1.0]})

    def add_prior_node(self, rv_name, prob_dist):
        """ adds a node to joint distribution table

        Args:
            rv_name (str): name of random variable (must be unique in df_joint)
            prob_dist (dict): keys are outcomes of random variable, values are
                probability of each
        """
        assert rv_name not in self.df_joint.columns, \
            f"non-unique node: {rv_name}"
        
        row_list = list()
        for key, value in prob_dist.items():
            new_row = {"prob": value, rv_name: key}
            row_list.append(new_row)
            
        self.df_joint = pd.DataFrame(row_list)    

    def add_conditional_node(self, cond_dist):
        """ adds a nodes to joint distribution table

        Args:
            cond_dist (ConditionalProb): a conditional probability of some new
                random variable.  (conditioned on random variables already in
                df_joint)
        """
        # check that all conditioned variables are in joint already
        assert set(cond_dist.condition_list).issubset(self.df_joint.columns), \
            f"condition rvs not in joint table: {cond_dist.condition_list}"
        
        # check that target variable is not in joint already
        assert cond_dist.target not in self.df_joint.columns, \
            f"random variable already in network: {cond_dist.target}"
        
        table = copy(self.df_joint)
        row_list = list()
        
        # computes conditional probabilities, adds new row to joint table
        for item in cond_dist.condition_list:
            for outcome, prob in cond_dist.cond_prob_dict.items():
                for idx, row in self.df_joint.iterrows():
                    for key, value in prob.items():
                        if set(row).issuperset(outcome):
                            star = row["prob"]
                            cond = row[item]
                            
                            new_row = {"prob": star * value,
                                       item: cond,
                                       cond_dist.target: key}
                            row_list.append(new_row)
        
        # struggling to merge table and row_list
        self.df_joint = pd.DataFrame(row_list)

    def get_prob(self, state):
        """ sums all rows which satisfy state (marginalization)

        Args:
            state (dict): keys are random variable, values are corresponding
                outcomes
                
        Returns:
            prob (float): probability of the given state
        """

    def get_conditional_prob(self, state, condition):
        """ computes conditional probability of state given condition:

        P(ABC|XYZ) = P(ABCXYZ) / P(XYZ)

        above ABC are state variables while XYZ are conditional variables

        Args:
            state (dict): keys are random variable, values are corresponding
                outcomes
            condition (dict): keys are random variable, values are
                corresponding outcomes
                
        Returns:
            prob (float): probability of the given state given condition
        """
        # check that no variable is in state & conditional
        rv_double = set(state.keys()).intersection(condition.keys())
        assert not rv_double, \
            f"same random variable before & after conditional: {rv_double}"


# # Part 1: `BayesNetwork.add_prior_node` (20 points)
# 
# We validate whether the nodes have been added properly by constructing a known example: 
# 
# <img src="https://miro.medium.com/max/640/1*9OsQV0PqM2juaOtGqoRISw.jpeg" width=500>
# 
# and comparing output `bayes_net.df_joint` to expected dataframes, which are stored in the [expected_csv](expected_csv) folder.

# In[2]:


# for example, after adding the cloudy node to the network, bayes_net.df_joint should look as below:
df_expected = pd.read_csv('expected_csv/prob_cloudy.csv', index_col=False)
df_expected


# In[3]:


# build bayes net with cloudy node
bayes_net = BayesNetwork()
bayes_net.add_prior_node('Cloudy', prob_dist={'c0': .5, 'c1': .5})

# manually check output dataframe (just this first time, to see how to debug below)
bayes_net.df_joint


# In[4]:


from df_compare import assert_df_equal_no_idx

assert_df_equal_no_idx(bayes_net.df_joint, df_expected)


# # Part 2: `BayesNetwork.add_conditional_node` (25 points)
# 
# Hint:
# - Inspect and study the given output DataFrames via their [expected_csv](expected_csv) before implementing!

# In[5]:


from conditional import ConditionalProb

# add rain conditional prob
cond_prob_rain = \
    ConditionalProb(target='Rain',
                    condition_list=['Cloudy'],
                    cond_prob_dict={('c1',): {'r1': .8, 'r0': .2},
                                    ('c0',): {'r1': .2, 'r0': .8}})

bayes_net.add_conditional_node(cond_prob_rain)
print(bayes_net.df_joint)

# check that rain conditional prob was added properly
df_joint_expected = pd.read_csv('expected_csv/prob_cloudy_rain.csv', index_col=False)
assert_df_equal_no_idx(df_joint_expected, bayes_net.df_joint)


# In[6]:


df_joint_expected


# In[7]:


# add sprinkler conditional prob
cond_prob_sprinkler = \
    ConditionalProb(target='Sprinkler',
                    condition_list=['Cloudy'],
                    cond_prob_dict={('c1',): {'s1': .1, 's0': .9},
                                    ('c0',): {'s1': .5, 's0': .5}})
bayes_net.add_conditional_node(cond_prob_sprinkler)
print(bayes_net.df_joint)

# check that sprinkler conditional prob was added properly
df_joint_expected = pd.read_csv('expected_csv/prob_cloudy_rain_sprinkler.csv', index_col=False)
assert_df_equal_no_idx(df_joint_expected, bayes_net.df_joint)


# In[8]:


df_joint_expected


# In[9]:


# add wet grass conditional prob
cond_prob_grass_wet = \
    ConditionalProb(target='WetGrass',
                    condition_list=['Rain', 'Sprinkler'],
                    cond_prob_dict={('r1', 's1'): {'w1': .99, 'w0': .01},
                                    ('r0', 's1'): {'w1': 0.9, 'w0': .1},
                                    ('r1', 's0'): {'w1': 0.9, 'w0': .1},
                                    ('r0', 's0'): {'w1': 0.0, 'w0': 1}})
bayes_net.add_conditional_node(cond_prob_grass_wet)

# check that wet grass conditional prob was added properly
df_joint_expected = pd.read_csv('expected_csv/prob_cloudy_rain_sprinkler_grass.csv', index_col=False)
assert_df_equal_no_idx(df_joint_expected, bayes_net.df_joint)


# In[10]:


df_joint_expected


# # Part 3: `BayesNet.get_prob` (20 points)

# In[ ]:


from math import isclose

assert isclose(bayes_net.get_prob({'Cloudy': 'c1'}), .5)

assert isclose(bayes_net.get_prob({'Sprinkler': 's1', 'Cloudy': 'c1'}), .05)
assert isclose(bayes_net.get_prob({'Sprinkler': 's1', 'Cloudy': 'c0'}), .25)
assert isclose(bayes_net.get_prob({'Sprinkler': 's1'}), .3)

assert isclose(bayes_net.get_prob({'Rain': 'r1', 'Cloudy': 'c1'}), .4)
assert isclose(bayes_net.get_prob({'Rain': 'r1', 'Cloudy': 'c0'}), .1)
assert isclose(bayes_net.get_prob({'Rain': 'r1'}), .5)


# #### extra math note (not needed for HW completion, helpful for probability fluency though)
# 
# The chunks of three assert statements immediately above demonstrate marginalization: 
# 
# - there's only two ways sprinkler is on: 
#     - when its cloudy or clear outside (.3 = .05 + .25)
# - there's only two ways its raining:     
#     - when its cloudy or clear outside (.5 = .1 + .4)

# # Part 4: `BayesNet.get_conditional_prob` (15 points)
# 
# To validate `.get_conditional_prob()` we reproduce known conditional probs from the bayes net definition:

# In[ ]:


# whats the prob the sprinkler is on given its cloudy?
assert isclose(bayes_net.get_conditional_prob(state={'Sprinkler': 's1'}, condition={'Cloudy': 'c1'}), .1)


# In[ ]:


# whats the prob its not raining given its not cloudy?
assert isclose(bayes_net.get_conditional_prob(state={'Rain': 'r0'}, condition={'Cloudy': 'c0'}), .8)


# In[ ]:


# whats the prob lawn is wet given sprinkler is on and its raining?
assert isclose(bayes_net.get_conditional_prob(state={'WetGrass': 'w1'}, condition={'Sprinkler': 's1',
                                                                                    'Rain': 'r1'}), .99)


# # Part 5: Gardening (15 points)
# 
# A gardener wants their newly planted lawn to have (at least) a 70% chance of being wet while using their sprinkler as little as possible, to conserve water.  Each morning they step outside their house and observe only if it is cloudy or not.  With only this evidence, they want to know whether they must turn their sprinkler on.
# 
# - on clear days, should the gardener turn on their sprinkler?
# - on cloudy days, should the gardener turn on their sprinkler?
# - is it possible for the gardener to always ensure at least 70% chance of having a wet lawn?
# 
# Call a few methods of the bayes net above to investigate the questions immediately above.  Write a summary of results in 2-3 sentences which is easily understood by a garener who knows little of probability or Bayes Nets.

# # Part 6: Memory Analysis (5 points)
# 
# Let's consider the liver disease bayes net example shown in class.  Assuming it has 40 total nodes, and each is binary, how much memory would it cost to store the probability column of `df_joint` as shown above?  Assume that every combination of variables must be stored as a float which uses `np.ones(1).nbytes / 1e6` megabytes of space.
# 
# Summarize your computation in 2 sentences so a non-technical reader can understand the drawback.  (Note: this memory problem lies with our implementation, there are methods to avoid it)
# 
# Hint:
# - its a big number, don't try this line of code as you'll run out of memory before you get an answer:
#     - `np.ones(2 ** 40).nbytes / 1e6` megabytes of space
