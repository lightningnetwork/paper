# 5 The Shadowchain: A Bitcoin Overlay Appli- cation Framework

In this section, we present the concept of a Shadowchain, a non-custodial ap- plication overlay framework that we’ll use to construct a concrete instantiation of a CLM. We note that shadowchains may also be of independent interest, as they’re a novel way to layer more complex interactions on top of the base Bit- coin blockchain. Shadowchains as we present them can be implemented on the base Bitcoin blockchain today without any additional changes or enhancements.

However, further extensions to Bitcoin such as cross-input signature aggrega- tion and covenants could serve to dramatically improve scalability properties of shadowchains.

## 5.1 High-Level Description

First, we provide a high-level description of the shadowchain application frame- work.

The Shadowchain Usecase. A shadowchain can be used to implement non-custodial smart contract systems on top of the base Bitcoin blockchain. Typically, one would opt for a shadowchain if the complexity of the state tran- sition logic of the smart contract system could not be fully expressed using  the base Bitcoin Script. Shadowchains allow an application designer to use the Bitcoin blockchain for censorship resistant settlement, while pushing the more complex portions of the application (state, logic, etc.) oﬀ-chain.

Shadowchain Roles & Lifted UTXOs. A shadowchain has two primary classes of agents: users, and the orchestrator. The orchestrator deﬁnes the state transition function of the shadowchain, a set of non-trusted initialization parameters, and upgrade mechanisms. A user is able to join a shadowchain  by ”lifting” their UTXOs into the higher-level shadowchain. The process of lifting (deﬁned further below) entails the user placing funds within a time-lock released, multi-signature output that enforces cooperation between the user and the shadowchain orchestrator.

Shadowchain Operation. The shadowchain orchestrator accepts trans- action data from users and periodically proposes a new shadowchain block. A shadowchain block takes as input the set of Lifted UTXOs that accepted the latest block proposals, and produces a set of new UTXOs, which are the end state after the state transition function has been evaluated. A shadowchain is even permitted to use multiple distinct state transition functions. As user funds cannot move without both multi-sig signatures, users are able to fully vali- date (possibly using techniques such as zero knowledge proofs that the resulting UTXO state was properly derived from the known state transition function. Note that due to this structure, complex ”exit-games”, or fraud proofs are not required as a user simply won’t sign oﬀ on a fraudulent state, and a user’s UTXO is always manifested (in its base form) on the main blockchain.

Ephemeral Lifted UTXOs. In the scenario that the shadowchain orches- trator disappears, or is unresponsive, users are able convert their lifted UTXO into regular ones by spending their coins after the time-lock has expired. This construct of an ephemeral lifted UTXO has a number of desirable properties  on the application level, as the time-locked commitment of funds can serve to mitigate a number of application-level issues such as spam or sybil resistance.

Shadowchain Cut-Through As the evolution of a state transition func- tion happens oﬀ-chain, it’s possible to coalesce several distinct shadowchain blocks into a single block that combines successive invocations of the state transition function. This technique is similar to transaction cut-through [18] but is performed in a multi-party setting. Leveraging this technique, the shadowchain orchestrator can optimistically treat the current latest shadowchain transaction in the mempool as an in-memory data structure to be updated oﬀ-chain (via transaction replacement techniques), with the state being ”written to disk”

once conﬁrmed. As a result, it’s possible to commit several shadowchain states (possibly hundreds) in a single logical Bitcoin transaction.

Shadowchain Upgrades. Finally, similar to the base blockchain, a shad- owchain can also be upgraded in a forward and backward compatible manner. In other words, it’s possible for a shadowchain orchestrator to soft-fork the state transition logic by restricting a valid state transition to enable new behavior.

Notably, the orchestrator can do this in a desynchronized manner such that only those wishing to use the features of the new state transition function need to adhere to the new rules. Additionally, an orchestrator can opt introduce new backward incompatible state transition functions. Note that because of the batching capabilities inherent in Bitcoin transactions, an orchestrator can com- mit multiple logical shadowchain blocks (with distinct state transition functions) in a single atomic Bitcoin transaction.

To summarize, the shadowchain application framework is a novel technique for constructing overlay applications on the base Bitcoin blockchain in a non- custodial manner. Shadowchains avoid the complexity of fraud proofs and exit games by ensuring that the user has custody of their funds at all times and is able to fully validate any proposed state transition. Shadowchains are able to compress several logical state transitions into a single Bitcoin transaction using a multi-party cut-through technique. An orchestrator of a shadowchain is also able to upgrade the state transition logic on the ﬂy, in a purely oﬀ-chain manner.

## 5.2 Comparison To Related Frameworks

## 5.3 The Shadowchain Framework

In this section, we present the abstract shadowchain application framework. Applications are intended to use this framework, providing implementations of speciﬁed virtual functions to fully specify and execute their application.

### 5.3.1 Shadowchain Orchestrator

First, we introduce the glue that keeps a shadowchain together, the orchestrator:

### Deﬁnition 5.1. (Orchestrator).

The Orchestrator is a non-trusted entity at the root of a shadowchain, parametrized by its long-term public key: Ochain = PO.  The duty of an  Orchestrator is to propose new blocks (the result of a  state transition) to the set of live Lifted UTXOs that make up the shadowchain.

A given Orchestrator is a non-trusted entity, and can be uniquely identiﬁed by its long-term public key. The long-term public key PO can also be used to uniquely identify a given shadowchain, similar to the Genesis Block hash of a normal blockchain.

### 5.3.2 Lifted UTXOs

Next, we deﬁne the Lifted UTXO, which is the representation of a user’s state within a given shadow chain:

### Deﬁnition 5.2. (Lifted UTXO).

A Lifted UTXO is a tuple, φU = (Asat, Texpiry, Pu, Po), where:

❼ Asat is the size of a LO (Lifted UTXO) expressed in satoshis.

❼ Texpiry is the absolute expiry height of the LO, after which the owner is able to unilaterally move the funds back to the ”base” Bitcoin blockchain.

❼ Pu  is the public key of the end user, which is 1/2 of the public keys used in the public key script of the output which manifests this LO on the base blockchain.

❼ Po is the public key of the Orchestrator, typically derived from its base long-term key PO. This key will be used as the other half of the multi-sig script of the on-chain manifestation of the LO.

The construct of a Lifted UTXO is similar to the existing concept of a Fi- delity Bond [13] with an application-speciﬁc twist. This process is akin to creating a new ’account’ within a Shadowchain. The time-lock release nature of the UTXO means that a user can always recover funds if the Orchestrator be- comes unresponsive. In addition to this, a natural cost in the form of chain fees is added, which increases the barrier for potentially malicious users to interact with the shadow chain.

### 5.3.3 The Shadowchain

In this section, we present the abstract deﬁnition of a shadowchain, building upon the deﬁnition provided above. In addition to this, we describe the typical shadowchain lifecycle using the aid of some additional helper functions, which are also intended to be included in the application logic of the shadowchain.

#### Shadowchain Components

First, we deﬁne the core components of the shadowchain.

### Deﬁnition 5.3. (Shadowchain).

An instantiation of a Shadowchain is deﬁned as a tuple: Σ = (UL, UO, ∆F , Eexe, AT ), where:

❼ UL = φi, φn is the set of non-expired Lifted UTXOs observed by   the orchestrator.

❼ U0 is the current UTXO of the orchestrator, where they may accrue ap- plication level fees.

❼ ∆F  = 2∆f0 , … … … , ∆fn | is the set of current state transition functions.

❼ Eexe is the abstract execution environment of the shadowchain which all participants will use to verify the correctness of a proposed state transition.

❼ AT is the abstract form of the structure of the higher-level application’s fundamental transaction.

#### Shadowchain Algorithms

Given the above components, we deﬁne the operation of a shadowchain us- ing a series of polynomial-time algorithms segmented into the following logical categories:

❼ System Initialization: InitChain

❼ UTXO Management: (LiftUTXO, UnliftUTXO, ExitChain)

❼ Block Proposal & Validation: (ConstructBlock, ProposeBlock)

❼ Chain Execution: CommitBlock

❼ Block Cut-Through: CoalesceBlocks

❼ Chain Upgrade: UpgradeChain

With behavior and semantics as expressed below.

#### System Initialization

Before a shadowchain can be used for a given application, the system must be initialized. This process results in the creation of the orchestrator’s long-term public key, the execution environment, and the set of state transition functions:

InitChain(1λ) (U0, P0, ∆F , Eexe). Given the security parameter λ (expressed in unary), the InitChain method returns the initial self-lifted UTXO of the orchestrator, the long-term public key of the orchestrator, and the set of initial state transition functions along with the starting execution environment.

#### UTXO Management

Once a shadowchain has been initialized with a given set of parameters, users can begin lifting their UTXOs, enabling participation in shadowchain blocks and operations. The process of entering the shadowchain is referred to as UTXO Lifting, while exiting is the reverse process:

LiftUTXO(Texpiry, 2UN0 , . . . , UNn |, P0) ≥ φU . The LiftUTXO algorithm takes a series of normal UTXOs (UN ), the absolute expiration height of the UTXO,
and the long-term public key of the orchestrator P0, outputting a new Lifted UTXO for the target user. The total value of the set of input UTXOs must be greater-than-or-equal to the value of the resulting Lifted UTXO.

ExitChain(φU , Bheight) ≥ UN . Given a lifted UTXO with expiration height Texpiry > Bheight, where Bheight, the ExitChain method spends an existing lifted UTXO and resolves the user’s funds in a regular unencumbered UTXO. Users will use this algorithm if they wish to exit the chain in cases where the orchestrator is no longer being responsive.

UnliftUTXO(φU ) UN . Given a  lifted  UTXO,  the  UnliftUTXO method create a new normal un-lifted UTXO that returns all funds to the user.  This   is the optimistic version of the ExitChain algorithm, in that it requires coop- eration from the orchestrator as the time-release clause of the Lifted UTXO’s script is not yet unlocked.

#### Block Proposal & Validation

Once a shadowchain has a suﬃcient number of lifted UTXOs and the system has been fully initialized, block proposal and validation can commence. This process is similar to the process of nodes broadcasting transactions, and miners ordering them within blocks in the base Bitcoin system:

ConstructBlock(φlive, Txn, Eexe, ∆F )  BS.  Given inputs of the set of  ’live’ Lifted UTXOs, the set of transactions belonging to the live UTXOs, the execution environment, and the current set of valid state transition functions, the ConstructBlock outputs a valid shadowchain block to extend the main chain where:

❼ φlive = live(  φU0 ,    , φUa     is the set of ’live’ Lifted UTXOs where the live algorithm uses a heartbeat-like protocol to detect the current set of active users.

❼ Txn is the application-speciﬁc transaction format used within the shad- owchain.

❼ BS = (Txn, 2φU0 , … … … , φUa |, ∆f , 2φ/U  , … … … , φ/U    |, UA), is the shadowchain

block itself, which is composed of the set of application transaction, input Lifted UTXOs, the resulting output UTXOs after applying the set of state transition functions, and UA any new application-speciﬁc UTXOs
produced as a result of the state transition function. Lifted UTXOs can be  consumed  fully  by  the  state  transitions,  therefore λ2φU0 , … … … , φUa |λ-λ 2φ/U0 , … … … , φ/Ua |λ must be given.

Once a block has been constructed, the orchestrator of the shadowchain now must propose said block to the set of live Lifted UTXOs before it can move onto the next phase of shadowchain operation. As a given user may reject a block, either implicitly due to being oﬄine, or explicitly due to a violation of the shadowchain consensus rules, this phase may be repeated a number of times. The operator will use the following algorithm to propose blocks:

ProposeBlock(BS, φlive) b. The ProposeBlock attempts to propose the given shadowchain block to the set of live Lifted UTXOs. The algorithm returns b = 1 if all of the participants accept the block. Once all participants have accepted the block, we can now proceed to the execution and block commitment phase.

#### Chain Execution

Once the operator has established a stable set of participants that accept the proposed shadowchain block, it can execute the block and commit it in the base Bitcoin blockchain:

CommitBlock(BS) (b, TXid). The CommitBlock takes a valid shadowchain block, and attempts to obtain all necessary witnesses to unlock the Lifted UTXOs to re-create them post state function application along with any new application-speciﬁc UTXOs. The algorithm returns b = 1 if the operator was able to succesfully obtain all necessary witnesses, and brodcasts the Bitcoin transaction that commits the shadowchain block. Otherwise, the operator may need to re-propose a new block to a subset of the live Lifted UTXOs.

#### Block Cut-Through

Given the structure of shadowchain blocks and state transition functions, it’s possible for a shadowchain orchestrator to compress several distinct shad- owchain blocks into a single instance that is equivalent to the application of successive state transition functions on a series of distinct shadowchain blocks:

CoalesceBlocks(  BS0 ,       , BSa     )       BS/  .    Given  a  series  of  consecutive shadowchain blocks, the CoalesceBlocks algorithms compresses each consec- utive block into a single block BSa that has an equivalent output state to the serial application of the state transition functions on each individual shad- owchain block.

The CoalesceBlocks algorithm is similar to the concept of transaction cut- through [18] for UTXO-based blockchains. Using this algorithm, the operator is able to propose a new equivalent block which produces the same set of Lifted UTXO outputs along with any other application-speciﬁc outputs produced by any of the intermediate blocks. This can be done post-facto, and also in an optimistic manner in order to coalesce several unconﬁrmed shadowchain blocks into a single one.

#### Chain Upgrade

The process of upgrading the chain in terms of the types of application-level transactions oﬀered, or the set of valid state transition functions used, can be done entirely oﬀ-chain in an asynchronous manner. In order to update the environment, state transition functions, or the application-level transactions, the orchestrator simply needs to utilize the following algorithm:

UpgradeChain(∆new, Ee/ xe, Tx/ n).  The  UpgradeChain is  an  algorithm that’s executed entirely in an oﬀ-chain manner allowing the operator of the shadowchain to upgrade some or all of: the application transaction data, the execution environment, and the set of state transition functions. Due to the nature of the shadowchain, users of this new functionality each user must update their local state. However, note that the Lifted UTXO remains the same, as the operator’s long-term public key remains unchanged.

### 5.3.4 Shadowchain Operation

In this section, we’ll put together the above algorithms to outline the main execution loop of the shadowchain from the perspective of the orchestrator as well as the participants. Shadowchain operation can be viewed as a linear deterministic state machine that uses the main Bitcoin blockchain to transition between states.

#### Orchestrator State Machine

The main Orchestrator State Machine loop ﬁrst attempts to process any new UTXO lifting requests and will optimistically attempt to merge any ex- isting unconﬁrmed shadowchain blocks that can be coalesced. Independent of either of these clauses, the system will then enter into its main loop from which the orchestrator will attempt to construct a new block. This loop will iterate through the set of live transactions, propose a block to the set of live UTXOs, ﬁlter any participants that reject the block, then attempt to commit the new block to the blockchain.

![Figure5_3_10](figures/figure5_3_10.png?raw=true "Figure5_3_10")

#### Participant State Machine

The main state machine of each shadowchain participant is essentially a mirror of the orchestrator state machine. First, it will process any requests to modify its existing Lifted UTXO, gather any unconﬁrmed transactions, then await a new block proposal from the orchestrator.

![Figure5_3_11](figures/figure5_3_11.png?raw=true "Figure5_3_11")
