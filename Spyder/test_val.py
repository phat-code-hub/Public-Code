import tensorflow as tf
tf.compat.v1.disable_eager_execution()
v=tf.Variable(0,name='v')
a=tf.constant(10,name='10')
b=tf.constant(20,name='20')
mul_op=tf.multiply(a,b,name='mul')
assign_op=tf.compat.v1.assign(v,mul_op)
sess=tf.compat.v1.Session()
sess.run(assign_op)
tf.compat.v1.summary.FileWriter('./logs',sess.graph)
res=sess.run(v)
print(res)