tf.reset_default_graph()

num_actions = 2
state_size = 4

path = "./cartpole-pg/"

training_episodes = 1000
max_steps_per_episode = 10000
episode_batch_size = 5

agent = Agent(num_actions, state_size)

init = tf.global_variables_initializer()

saver = tf.train.Saver(max_to_keep=2)

if not os.path.exists(path):
    os.makedirs(path)

with tf.Session() as sess:
    sess.run(init)

    total_episode_rewards = []

    gradient_buffer = sess.run(tf.trainable_variables())
    for index, gradient in enumerate(gradient_buffer):
        gradient_buffer[index] = gradient * 0

    for episode in range(training_episodes):

        state = env.reset()

        episode_history = []
        episode_rewards = 0

        for step in range(max_steps_per_episode):

            if episode % 100 == 0:
                env.render()

            action_probabilities = sess.run(agent.outputs, feed_dict={agent.input_layer: [state]})
            action_choice = np.random.choice(range(num_actions), p=action_probabilities[0])

            state_next, reward, done, _ = env.step(action_choice)
            episode_history.append([state, action_choice, reward, state_next])
            state = state_next

            episode_rewards += reward

            if done or step + 1 == max_steps_per_episode:
                total_episode_rewards.append(episode_rewards)
                episode_history = np.array(episode_history)
                episode_history[:, 2] = discount_normalize_rewards(episode_history[:, 2])

                ep_gradients = sess.run(agent.gradients, feed_dict={agent.input_layer: np.vstack(episode_history[:, 0]),
                                                                    agent.actions: episode_history[:, 1],
                                                                    agent.rewards: episode_history[:, 2]})
                for index, gradient in enumerate(ep_gradients):
                    gradient_buffer[index] += gradient

                break

        if episode % episode_batch_size == 0:

            feed_dict_gradients = dict(zip(agent.gradients_to_apply, gradient_buffer))

            sess.run(agent.update_gradients, feed_dict=feed_dict_gradients)

            for index, gradient in enumerate(gradient_buffer):
                gradient_buffer[index] = gradient * 0

        if episode % 100 == 0:
            saver.save(sess, path + "pg-checkpoint", episode)
            print("Average reward / 100 eps: " + str(np.mean(total_episode_rewards[-100:])))
