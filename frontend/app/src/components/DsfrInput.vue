<script setup lang="ts">
import { reactive, ref, watch } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrInput } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '../streamlit'
import type { ComponentProps } from '../types/ComponentProps'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		// Props
		labelVisible?: boolean
		hint?: string
		modelValue?: string
		id?: string
		descriptionId?: string
		isInvalid?: boolean
		isValid?: boolean
		isWithWarning?: boolean
		labelClass?: string
		wrapperClass?: string
		// Slots
		label?: string
		requiredTip?: string
	}>
>()

const checked = ref('')

watch(
	() => checked,
	(value) =>
		{
			Streamlit.setComponentValue(value.value)
		},
	{ immediate: true },
)
</script>

<template>
	<div class="component">
		<DsfrInput v-bind="props.args" v-model="checked">
			<template #label v-if="props.args.label">
				{{ props.args.label }}
			</template>
			<template #required-tip v-if="props.args.requiredTip">
				{{ props.args.requiredTip }}
			</template>
		</DsfrInput>
	</div>
</template>
